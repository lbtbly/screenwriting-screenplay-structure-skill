#!/usr/bin/env python3
"""
extract-structure.py — measurement pass for the structure-audit skill.

Takes a screenplay PDF (or a .txt already produced by `pdftotext -layout`) and
reports the numbers §1 of audit-procedure.md requires:

  * total physical pages
  * printed page numbers, the printed<->PDF offset, and every point the offset
    drifts (A-pages, unnumbered inserts, omitted pages)
  * scene headings with printed + physical page positions
  * scene count, average scene length, longest scene, longest stretch with no
    scene change
  * printed act labels (ACT ONE / TEASER / COLD OPEN / END OF ACT / TAG / PART)

Why a script and not greps: `pdftotext` writes a form feed (\\x0c) immediately
before the first character of every page, and on most screenplays that first
character *is* the page number. A line-anchored grep therefore never matches it
(`^` sits before the form feed, not after it), and `[\\f \\t]` inside a POSIX
bracket expression matches a literal `f`, not a form feed. The only reliable fix
is to split the text on \\x0c in a real language, which is what this does.

MEASURED VERSUS INFERRED
------------------------
This skill's doctrine is measure before judging, so the output separates what
was read off the page from what was worked out. Report these fields; do not
consume them silently.

  Numbers read from        which zone the page numbers came from (header, or
                           header + footer on a script that paginates at the
                           foot, e.g. Only Murders in the Building)
  Page numbers asserted    read + interpolated + back-extrapolated
  READ off the page        count and % — MEASURED. Read from a page's own header
  INFERRED                 count and % — NOT MEASURED, split into
                             interpolated    both neighbours were read
                             back-extrapolated  before the first read number
                                                (page 1 is usually unnumbered)
  NUMBERING CONFIDENCE     high  >= 90% read
                           medium >= 60% read
                           low   <  60% read
  Printed body pages       always the LAST DIRECTLY READ printed number, with a
                           one-line `basis` saying so. Never extrapolated.
  Trailing unnumbered      physical sheets after the last read number. Reported
                           as unnumbered, NEVER renumbered: a publisher's back
                           cover is not printed page 142.

A `!! WARNING` block fires, and must be quoted in the report's Assumptions
section, whenever confidence is below high, whenever no printed number was read
at all, whenever trailing sheets are unnumbered, and whenever a printed number
appears on more than one sheet. In the scene and act lists a page label written
`~57` was INFERRED and `—` means the page is unnumbered; a label with no prefix
was read off that page. Never cite a `~` page as a measurement.

Usage:
    python3 extract-structure.py SCRIPT.pdf
    python3 extract-structure.py SCRIPT.txt          # already pdftotext -layout
    python3 extract-structure.py SCRIPT.pdf --json   # machine-readable
    python3 extract-structure.py SCRIPT.pdf --scenes # full scene list, no truncation
    python3 extract-structure.py SCRIPT.pdf --dump-text OUT.txt

In --json, the same information lives at numbering.confidence (with
thresholds_pct_read), numbering.printed_body_pages_basis,
numbering.trailing_unnumbered_pages, scenes.average_length_basis, and the
top-level `warnings` list. Every scene and act heading carries printed_basis.

Exit codes: 0 ok · 2 no text layer (scanned) · 3 unreadable input.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

FF = "\x0c"

# Confidence thresholds, in PERCENT OF THE DENOMINATOR whose printed page number
# was read directly off the page rather than inferred. Stated in every report so
# a downstream reader can see the bar, not just the verdict.
CONF_HIGH = 90.0  # >= 90% read  -> high
CONF_MEDIUM = 60.0  # >= 60% read  -> medium; below that -> low

# ----------------------------------------------------------------------------
# 0. Text acquisition
# ----------------------------------------------------------------------------


def pdf_page_count(path):
    """Page count straight from the PDF, independent of the text layer."""
    if shutil.which("pdfinfo"):
        try:
            out = subprocess.run(
                ["pdfinfo", path], capture_output=True, text=True, timeout=120
            ).stdout
            m = re.search(r"^Pages:\s+(\d+)", out, re.M)
            if m:
                return int(m.group(1))
        except Exception:
            pass
    try:
        import pypdf

        return len(pypdf.PdfReader(path).pages)
    except Exception:
        return None


def extract_text(path):
    """Return (text, method). Layout mode is mandatory: without it the
    right-margin page numbers and scene numbers merge into the body text."""
    if path.lower().endswith(".txt"):
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read(), "pre-extracted .txt"

    if shutil.which("pdftotext"):
        tmp = tempfile.NamedTemporaryFile(suffix=".txt", delete=False)
        tmp.close()
        try:
            subprocess.run(
                ["pdftotext", "-layout", path, tmp.name],
                capture_output=True,
                timeout=600,
                check=False,
            )
            with open(tmp.name, encoding="utf-8", errors="replace") as fh:
                return fh.read(), "pdftotext -layout"
        finally:
            os.unlink(tmp.name)

    try:  # fallback only; layout fidelity is lower
        import pdfplumber

        pages = []
        with pdfplumber.open(path) as pdf:
            for pg in pdf.pages:
                pages.append(pg.extract_text(layout=True) or "")
        return FF.join(pages), "pdfplumber (fallback — layout approximate)"
    except Exception as exc:
        sys.stderr.write(f"ERROR: cannot extract text: {exc}\n")
        sys.exit(3)


def split_pages(text):
    """Split on the form feed. pdftotext emits a trailing FF after the last
    page, so the final element is empty and must be dropped."""
    if FF not in text:
        return [text], True  # no page breaks at all
    pages = text.split(FF)
    if pages and not pages[-1].strip():
        pages.pop()
    return pages, False


# ----------------------------------------------------------------------------
# 1. Scanned / no-text-layer detection
# ----------------------------------------------------------------------------


def text_layer_report(pages, phys_pages):
    chars = sum(len(re.sub(r"\s", "", p)) for p in pages)
    n = max(len(pages), 1)
    per_page = chars / n
    empty = sum(1 for p in pages if len(re.sub(r"\s", "", p)) < 20)
    # A real screenplay page carries 700-2500 non-space characters; a multi-cam
    # page (double-spaced, wide margins) still carries 400+.
    scanned = per_page < 120 or empty >= 0.8 * n
    return {
        "chars_total": chars,
        "chars_per_page": round(per_page, 1),
        "pages_effectively_empty": empty,
        "no_text_layer": scanned,
    }


# ----------------------------------------------------------------------------
# 2. Printed page numbers
# ----------------------------------------------------------------------------

# Punctuation that can sit between a page label and its number, or trail it.
# Includes the quote/comma debris OCR leaves behind: `p" 23"`, `p,.  82 .`
_PUNC = r"[.,:;'\"‘’“”·•*_-]"

# whole line is the number:      "  47."   "  47"   "  16 A"   "112A."   "p. 2."   "p.2"
RE_NUM_WHOLE = re.compile(
    r"^\s*(?:[pP](?:g|age|AGE)?" + _PUNC + r"{0,3}\s*)?"
    r"(\d{1,4})\s?([A-Za-z])?\s*" + _PUNC + r"{0,3}\s*$"
)
# number carries an explicit page label at the end of a running header:
#   'MULAN EIGHTH DRAFT      12/21/96     p. 2.'
#   "MULAN EIGH'rH DRAFT     12/21/96     p . 38."      (OCR: space inside "p.")
#   'MULAN EIGHTH DRAFT      12/21/96     p" 23"'       (OCR: '.' read as '"')
#   "MULAN EIGH'l'H DRAFT     6/6/97      p,.   82 ."   (OCR: '.' read as ',.')
# This is the case a bare `\s{2,}` tail regex cannot see: only ONE space separates
# the label from the number, so the number never looks like a right-aligned token.
RE_NUM_LABEL = re.compile(
    r"(?:^|\s)[pP](?:g|age|AGE)?(?:" + _PUNC + r"|\s){0,6}"
    r"(\d{1,4})\s?([A-Za-z])?\s*" + _PUNC + r"{0,3}\s*$"
)
# number is the last token of a running header, right-aligned into the margin:
#   'THE ROOKIE - Ep. 101 - "PILOT" - Revised Network Draft - 1/21/18      2'
RE_NUM_TAIL = re.compile(
    r"(?:^|\s{2,})(\d{1,4})\s?([A-Za-z])?\s*" + _PUNC + r"{0,3}\s*$"
)

ROMAN = re.compile(r"^\s*([ivxlcIVXLC]{1,7})\s*\.?\s*$")


def suffix_value(sfx):
    if not sfx:
        return 0
    s = sfx.upper()
    # A -> 1, B -> 2 ... keep it ordinal so 12 < 12A < 12B < 13
    return min(26, ord(s[0]) - ord("A") + 1) if "A" <= s[0] <= "Z" else 0


def page_number_candidates(page, include_footer=False):
    """Candidates from the header zone (first 3 non-blank lines) of one page.

    With include_footer, the last 2 non-blank lines are scanned too. A few
    scripts paginate at the FOOT of the page (Only Murders in the Building
    centres `20.` on the last line and puts no number in its running header),
    and a header-only scan reads zero numbers on them. This is off by default and
    used only as a gated retry — see analyse() — because in a numbered shooting
    script the bottom margin also carries scene numbers, which increase
    monotonically and would otherwise compete with the real page numbering.

    Returns list of dicts: value (sortable float), num, suffix, weight, source.
    """
    out = []
    seen = set()
    nonblank = [l for l in page.split("\n") if l.strip()]
    zone = [(r, l, "line") for r, l in enumerate(nonblank[:3])]
    if include_footer:
        tail = nonblank[-2:] if len(nonblank) > 3 else []
        zone += [(len(tail) - 1 - i, l, "foot") for i, l in enumerate(tail)]
    for rank, line, where in zone:
        stripped = line.strip()
        if ROMAN.match(stripped) and not stripped[0].isdigit():
            continue  # front-matter roman numeral: real, but not body numbering
        for regex, kind, base in (
            (RE_NUM_WHOLE, "whole-line", 1.00),
            (RE_NUM_LABEL, "labelled", 0.95),
            (RE_NUM_TAIL, "header-tail", 0.85),
        ):
            m = regex.match(line) if kind == "whole-line" else regex.search(line)
            if not m:
                continue
            num = int(m.group(1))
            sfx = (m.group(2) or "").upper()
            if num == 0 or num > 400:
                continue
            if sfx and suffix_value(sfx) == 0:
                sfx = ""
            key = (num, sfx)
            if key in seen:
                continue
            seen.add(key)
            weight = base * (1.0 if rank == 0 else 0.55 if rank == 1 else 0.35)
            out.append(
                {
                    "value": num + 0.01 * suffix_value(sfx),
                    "num": num,
                    "suffix": sfx,
                    "weight": weight,
                    "source": f"{kind}/{where}{rank + 1}",
                    "raw": stripped[:70],
                }
            )
    return out


def reconcile_numbering(cands_per_page):
    """Pick one candidate per page so the sequence is non-decreasing and tracks
    physical progression. Printed numbering may *lag* physical pages (A-pages,
    unnumbered inserts) but must never run ahead of it, so leading is penalised
    hard and lagging softly. Longest-best-path DP over candidates.

    A REPEATED number on two adjacent sheets (Lady Bird prints `30.` twice, Mulan
    prints `p. 101.` twice) is a real and common binding artefact, not noise, and
    it is the direct cause of offset drift. The DP therefore admits an equal step
    between adjacent physical pages at a small penalty; forbidding it — as a
    strictly-increasing chain does — silently deletes the evidence of the drift
    and of the duplicate at the same time."""
    nodes = []  # (page_index, candidate)
    for p, cands in enumerate(cands_per_page):
        for c in cands:
            nodes.append((p, c))
    if not nodes:
        return {}

    best = [n[1]["weight"] for n in nodes]
    prev = [-1] * len(nodes)
    for j, (p2, c2) in enumerate(nodes):
        for i, (p1, c1) in enumerate(nodes):
            if p1 >= p2 or c2["value"] < c1["value"]:
                continue
            dp = p2 - p1
            dv = c2["value"] - c1["value"]
            if dv == 0:
                # Same printed number twice. Only believable on consecutive
                # sheets, and only when both reads are strong. The lag penalty is
                # NOT also charged here: for a repeat, the one-page lag IS the
                # observation, so charging for it on top of `dup` makes including
                # a genuine duplicate score worse than dropping it — which is how
                # the duplicate and the drift it causes both vanished before.
                if dp != 1 or c1["weight"] < 0.5 or c2["weight"] < 0.5:
                    continue
                score = best[i] + c2["weight"] - 0.20
                if score > best[j]:
                    best[j] = score
                    prev[j] = i
                continue
            lead = max(0.0, dv - dp)  # printed ahead of physical: implausible
            lag = max(0.0, dp - dv)  # A-pages / unnumbered: normal
            score = best[i] + c2["weight"] - 3.0 * lead - 0.35 * lag
            if score > best[j]:
                best[j] = score
                prev[j] = i

    end = max(range(len(nodes)), key=lambda k: best[k])
    chain = []
    while end != -1:
        chain.append(nodes[end])
        end = prev[end]
    chain.reverse()
    return {p: c for p, c in chain}


def build_page_map(pages, cands_per_page):
    """printed[] per physical page.

    Every entry carries a `basis` saying HOW the number was obtained:

      READ            the number was read off that page's header. Measured.
      INTERPOLATED    both neighbours were read and the gap is a clean run.
      INTERPOLATED?   the gap is ambiguous (A-pages or omissions inside it);
                      no number is asserted at all, only an ordering.
      EXTRAPOLATED-B  before the first read number (page 1 is conventionally
                      unnumbered). Inferred from the offset, not read.

    There is deliberately no forward extrapolation. Pages after the last read
    number are left as None and reported as `trailing_unnumbered_pages`: a
    publisher's back cover (Parasite PDF p.144) is not printed page 142, and
    inventing a number for it inflates the denominator every percentage in the
    report is divided by."""
    anchors = reconcile_numbering(cands_per_page)
    printed = [None] * len(pages)
    for p, c in anchors.items():
        printed[p] = {
            "num": c["num"],
            "suffix": c["suffix"],
            "label": f"{c['num']}{c['suffix']}",
            "value": c["value"],
            "inferred": False,
            "basis": "READ",
            "raw": c["raw"],
        }
    # interpolate gaps between anchors
    idx = sorted(anchors)
    for a, b in zip(idx, idx[1:]):
        gap = b - a - 1
        if gap <= 0:
            continue
        lo, hi = printed[a]["value"], printed[b]["value"]
        if hi - lo == gap + 1:  # clean run of plain numbers
            for k in range(1, gap + 1):
                n = printed[a]["num"] + k
                printed[a + k] = {
                    "num": n,
                    "suffix": "",
                    "label": str(n),
                    "value": float(n),
                    "inferred": True,
                    "basis": "INTERPOLATED",
                    "raw": "",
                }
        else:  # ambiguous (A-pages or omissions inside the gap)
            for k in range(1, gap + 1):
                printed[a + k] = {
                    "num": None,
                    "suffix": "",
                    "label": "?",
                    "value": lo + (hi - lo) * k / (gap + 1),
                    "inferred": True,
                    "basis": "INTERPOLATED?",
                    "raw": "",
                }
    # extrapolate backward before the first anchor: page 1 of a screenplay is
    # conventionally unnumbered, so the first *printed* number is usually 2.
    # Stop at 1 — anything below that is front matter (title page, cast list).
    if idx:
        first = idx[0]
        for p in range(first - 1, -1, -1):
            n = printed[first]["num"] - (first - p)
            if n < 1:
                break
            printed[p] = {
                "num": n,
                "suffix": "",
                "label": str(n),
                "value": float(n),
                "inferred": True,
                "basis": "EXTRAPOLATED-BACK",
                "raw": "",
            }
    # NO forward extrapolation. See the docstring: trailing sheets that print no
    # number are reported as unnumbered, never renumbered.
    # With no anchors at all there is no "trailing" region — the whole file is
    # unnumbered, which is a different finding and is reported as its own warning.
    trailing = len(pages) - (idx[-1] + 1) if idx else 0
    leading = sum(1 for p in printed[: idx[0]] if p is None) if idx else 0
    return printed, anchors, trailing, leading


def offset_segments(printed):
    """Runs of constant offset. offset = physical(1-based) - printed number.

    READ pages only. Interpolated pages are, by construction, laid down at a
    constant offset between their anchors, so including them cannot reveal drift
    and can only hide it: a script whose numbers were 97% interpolated (Mulan,
    before the header regex was fixed) reported `drift 0` on a script that drifts.
    Drift is a claim about what is printed; only printed numbers may support it."""
    segs = []
    for p, pr in enumerate(printed):
        if not pr or pr["num"] is None or pr["basis"] != "READ":
            continue
        off = (p + 1) - pr["num"]
        if segs and segs[-1]["offset"] == off and segs[-1]["last_phys"] == p:
            segs[-1]["last_phys"] = p + 1
            segs[-1]["last_printed"] = pr["label"]
            continue
        if segs and segs[-1]["offset"] == off:
            segs[-1]["last_phys"] = p + 1
            segs[-1]["last_printed"] = pr["label"]
        else:
            segs.append(
                {
                    "offset": off,
                    "first_phys": p + 1,
                    "last_phys": p + 1,
                    "first_printed": pr["label"],
                    "last_printed": pr["label"],
                }
            )
    return segs


# ----------------------------------------------------------------------------
# 3. Scene headings
# ----------------------------------------------------------------------------

TIME_TAIL = re.compile(
    r"[-–—]\s*(DAY|NIGHT|MORNING|EVENING|AFTERNOON|DUSK|DAWN|LATER|"
    r"CONTINUOUS|SAME|MOMENTS LATER|MAGIC ?HOUR|SUNSET|SUNRISE|PRE ?DAWN|"
    r"NIGHT ?TIME|DAY ?TIME|MIDNIGHT)\b",
    re.I,
)
# Lady Bird style: "INT. KITCHEN. DAY." — period-separated, no dash
TIME_TAIL_DOT = re.compile(
    r"\.\s*(DAY|NIGHT|MORNING|EVENING|AFTERNOON|DUSK|DAWN|CONTINUOUS)\s*\.?\s*$", re.I
)

# leading scene number of a numbered shooting script:
#   "23      INT. SHAKESPEARE & CO. - DAY                         23"
#   "*87a INT. DEN                                             87a*"
#   "__ 103   INT. _SALLY.'S BATHROOJ!"      (OCR debris before the number)
RE_SCENE_NO = re.compile(
    r"^(?P<pre>\s{0,40}[*_.,'\"·;:|~^\-]{0,6}\s{0,6})"
    r"(?P<no>\d{1,3}[A-Za-z]{0,2})[.)]?"
    r"(?P<gap>\s+)(?P<body>\S.*)$"
)

OMITTED = re.compile(r"^(OMIT|OMMIT|O\W?[IM1l]{1,3}T|DELETED)\b", re.I)


def is_continuation(body):
    """`CONTINUED:` and its OCR mutations — CONTIHUED:, CON'l'INUED:,
    CONTIHtJED:, CONTINtJED1. Compare the first six *letters* against CONTIN
    with the confusion-class distance; a real slugline never starts that way."""
    letters = re.sub(r"[^A-Za-z]", "", body)[:6].upper()
    if len(letters) < 5:
        return False
    return _fuzzy_dist(letters, "CONTIN", limit=1) <= 1

# character-confusion classes for OCR-tolerant matching of INT./EXT.
_CONFUSE = [
    set("IL1!|JRTFTIilrtj"),
    set("EFB8"),
    set("XKY%*"),
    set("O0QDCG"),
    set("UVY"),
    set("NMHR"),
    set("S5$"),
    set("TI7"),
]


def _same_class(a, b):
    if a == b:
        return True
    return any(a in cls and b in cls for cls in _CONFUSE)


def _fuzzy_dist(tok, target, limit=1):
    """Edit distance with OCR confusion classes counted as free substitutions."""
    n, m = len(tok), len(target)
    if abs(n - m) > limit:
        return limit + 1
    prev = list(range(m + 1))
    for i in range(1, n + 1):
        cur = [i] + [0] * m
        for j in range(1, m + 1):
            sub = 0 if _same_class(tok[i - 1], target[j - 1]) else 1
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + sub)
        prev = cur
    return prev[m]


def slug_prefix_kind(body):
    """Does `body` open with INT./EXT./I/E, allowing OCR corruption?

    Real corpus corruptions handled: IN'l'. IN'r. IN'!'. rNT. INT, EXT,
    E.XT. E:XT. Erl'. Err. UT. BXT. I/E. INT/EXT.
    """
    head = body[:14].upper()
    # I/E and INT./EXT. compounds first
    if re.match(r"^\s*(I\s*[/.]\s*E|E\s*[/.]\s*I)\b", head):
        return "I/E"
    m = re.match(r"^\s*(INT|EXT)[.\s]*/[.\s]*(EXT|INT)\b", head)
    if m:
        return "INT/EXT"
    tok = re.split(r"[\s]", body.strip(), 1)[0]
    core = re.sub(r"[^A-Za-z]", "", tok).upper()
    if not core or len(core) > 5:
        return None
    if core in ("INT", "INTERIOR"):
        return "INT"
    if core in ("EXT", "EXTERIOR"):
        return "EXT"
    # Fuzzy branch, deliberately narrow. Requirements, all of them:
    #   * the token still has exactly 3 letters (OCR mangles glyphs, not counts)
    #   * it ends in punctuation, like a real "INT."
    #   * a location follows it
    #   * the first letter is class-compatible with I or E
    # Without these, "ii." (a roman front-matter page number) scores as INT.
    # Shorter corruptions ("UT.", "IN'!'.") are caught by the numbered-slugline
    # detector instead, which is where they actually occur.
    if len(core) != 3:
        return None
    if not re.match(r"^[A-Za-z][^ ]{0,6}[.,:;]", tok):
        return None
    rest = body.strip()[len(tok):]
    if len(re.sub(r"[^A-Za-z]", "", rest)) < 3 or caps_ratio(body) < 0.6:
        return None
    if _same_class(core[0], "I") and _fuzzy_dist(core, "INT") <= 1:
        return "INT?"
    if _same_class(core[0], "E") and _fuzzy_dist(core, "EXT") <= 1:
        return "EXT?"
    return None


def caps_ratio(s):
    letters = [c for c in s if c.isalpha()]
    if not letters:
        return 0.0
    return sum(1 for c in letters if c.isupper()) / len(letters)


def strip_margin(body):
    """Drop the right-margin scene number and revision asterisk."""
    b = re.sub(r"\s{2,}\*?\s*\d{1,3}[A-Za-z]{0,2}[.·•*]?\s*\*?\s*$", "", body)
    return re.sub(r"[\s*·•]+$", "", b).rstrip()


def find_scene_headings(pages):
    """Return list of headings. Fires on three independent detectors:
    D1 plain INT./EXT. (OCR-tolerant) · D2 numbered-script slugline ·
    D3 caps line with a time-of-day tail."""
    heads = []
    numbered_hits = 0
    for p, page in enumerate(pages):
        lines = page.split("\n")
        nlines = max(len(lines), 1)
        for li, line in enumerate(lines):
            if not line.strip():
                continue
            raw = line.rstrip()
            indent = len(raw) - len(raw.lstrip())
            scene_no = None
            body = raw.strip()
            detector = None

            # A numbered shooting script indents the whole page block, so the
            # scene number can sit at column 25+. The reliable discriminator is
            # not the indent but the GAP: a slugline body follows its scene
            # number by a few spaces, a character cue is centred 20-40 columns
            # away with the same number repeated in both margins.
            m = RE_SCENE_NO.match(raw)
            if m and len(m.group("gap")) <= 8 and indent <= 40:
                cand_body = m.group("body").strip()
                if not is_continuation(cand_body):
                    scene_no = m.group("no")
                    body = cand_body

            body = strip_margin(body)
            body = re.sub(r"^[\s·•*_,'\"|~^]+", "", body)  # leading OCR debris
            if not body or is_continuation(body):
                continue
            if OMITTED.match(body):
                continue

            kind = slug_prefix_kind(body)
            if kind:
                detector = "D1-intext"
            elif scene_no is not None:
                # D2 — numbered shooting script. The scene number carries the
                # structural claim; the body only has to look like a heading.
                letters = re.sub(r"[^A-Za-z]", "", body)
                if (
                    len(letters) >= 4
                    and caps_ratio(body) >= 0.60
                    and len(body) <= 90
                    and indent <= 40
                    and not re.match(r"^\(", body)
                ):
                    detector = "D2-numbered"
                    numbered_hits += 1
            elif (
                indent <= 12
                and caps_ratio(body) >= 0.60
                and len(body) <= 90
                and (TIME_TAIL.search(body) or TIME_TAIL_DOT.search(body))
                and len(re.sub(r"[^A-Za-z]", "", body)) >= 6
            ):
                detector = "D3-timetail"

            if not detector:
                continue
            heads.append(
                {
                    "phys_page": p + 1,
                    "line": li,
                    "frac": li / nlines,
                    "scene_no": scene_no,
                    "kind": kind or ("numbered" if scene_no else "time-tail"),
                    "detector": detector,
                    "text": body[:88],
                }
            )
    return heads, numbered_hits


def _scene_key(no):
    m = re.match(r"^(\d{1,3})([A-Za-z]{0,2})$", no or "")
    if not m:
        return None
    sfx = m.group(2).upper()
    return (int(m.group(1)), suffix_value(sfx) if sfx else 0)


def filter_character_cues(heads):
    """In a numbered shooting script pdftotext also produces lines like

        20                        ALICE                          20

    — the scene number repeated in both margins beside a *character cue*.
    They pass the caps test, so a second net is needed: scene numbers only ever
    increase. A slugline's number is greater than every number seen so far; a
    cue repeats the number of the scene already running. Headings carrying an
    INT./EXT. token are exempt — that token is decisive on its own."""
    keep = []
    high = None
    for h in heads:
        key = _scene_key(h.get("scene_no"))
        if h["detector"] == "D2-numbered":
            if key is None or (high is not None and key <= high):
                continue
        if key is not None and (high is None or key > high):
            high = key
        keep.append(h)
    return keep


# ----------------------------------------------------------------------------
# 4. Act labels
# ----------------------------------------------------------------------------

ACT_PAT = re.compile(
    r"^\s*[*_.'\"|]{0,6}\s*"
    r"(?P<label>"
    # SHOW / EPISODE / PILOT are only act labels in "END OF ..." form —
    # bare PILOT on its own line is a character cue (The Rookie has one).
    r"END\s+OF\s+(SHOW|EPISODE|PILOT|PART|STORY)"
    r"|(END\s+OF\s+)?(TEASER|COLD\s+OPEN|PROLOGUE|EPILOGUE|TAG)"
    r"|(END\s+OF\s+)?ACT\s+(ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|[IVX]{1,4}|\d{1,2})"
    r"|(END\s+OF\s+)?PART\s+(ONE|TWO|THREE|FOUR|FIVE|SIX|[IVX]{1,4}|\d{1,2})"
    r"|MAIN\s+TITLES?"
    r")"
    r"[\s.:*_—–-]*$",
    re.I,
)


def find_act_labels(pages):
    out = []
    for p, page in enumerate(pages):
        lines = page.split("\n")
        nlines = max(len(lines), 1)
        for li, line in enumerate(lines):
            # strip the revision asterisk in the right margin BEFORE measuring
            # length, or "END OF ACT FOUR      *" is rejected as too long
            s = re.sub(r"[\s*·•]+$", "", line).strip()
            if not s or len(s) > 40:
                continue
            if caps_ratio(s) < 0.9:
                continue
            m = ACT_PAT.match(line)
            if m:
                out.append(
                    {
                        "phys_page": p + 1,
                        "line": li,
                        "frac": li / nlines,
                        "label": re.sub(r"\s+", " ", m.group("label").upper()),
                    }
                )
    return out


# ----------------------------------------------------------------------------
# 5. Assembly
# ----------------------------------------------------------------------------


def printed_of(printed, phys_page, frac=0.0):
    """Printed label + fractional printed position + how the label was obtained.

    A label that was not READ is prefixed with `~` so it cannot be copied into a
    report as a measured citation without the reader seeing that it is inferred.
    An unnumbered page returns `—`/UNNUMBERED and no position at all."""
    pr = printed[phys_page - 1] if 0 <= phys_page - 1 < len(printed) else None
    if not pr:
        return "—", None, "UNNUMBERED"
    label = pr["label"] if pr["basis"] == "READ" else "~" + pr["label"]
    return label, pr["value"] + frac, pr["basis"]


def body_range(printed, heads, acts):
    """First and last *body* page: front matter is everything before printed 1
    (or before the first scene heading if the script is unnumbered)."""
    first = None
    for p, pr in enumerate(printed):
        if pr and pr["num"] == 1 and not pr["inferred"]:
            first = p + 1
            break
    if first is None and heads:
        first = heads[0]["phys_page"]
    if first is None:
        first = 1
    last = len(printed)
    return first, last


def analyse(path, args):
    text, method = extract_text(path)
    pages, no_ff = split_pages(text)
    phys = pdf_page_count(path) if path.lower().endswith(".pdf") else None
    tl = text_layer_report(pages, phys)

    result = {
        "source": os.path.abspath(path),
        "extraction": method,
        "pdf_pages": phys,
        "text_pages": len(pages),
        "text_layer": tl,
    }

    if tl["no_text_layer"]:
        result["status"] = "NO TEXT LAYER"
        result["advice"] = (
            "This PDF is a scan/image with no extractable text "
            f"({tl['chars_per_page']} non-space chars per page across "
            f"{phys or len(pages)} pages). Every measurement below would be "
            "fabricated, so none is reported. Run OCR first "
            "(`ocrmypdf --force-ocr in.pdf out.pdf`, or `pdftoppm` + tesseract) "
            "and re-run this script on the OCR'd file. If OCR is unavailable, "
            "measure by hand and say so in the report's Assumptions section. "
            "Physical page count is the ONLY figure that can be trusted here."
        )
        return result

    warnings = []
    if no_ff:
        warnings.append(
            "NO FORM FEEDS in the text: page boundaries are unknown, so every "
            "per-page figure below is unreliable. Re-extract with "
            "`pdftotext -layout` from the PDF."
        )

    cands = [page_number_candidates(p) for p in pages]
    printed, anchors, trailing_unnumbered, leading_unnumbered = build_page_map(
        pages, cands
    )
    # Gated retry with the footer zone. Only attempted when the header pass has
    # read fewer than half the pages, and only adopted if it strictly reads more:
    # a script whose header numbering already works must not be disturbed by the
    # scene numbers that sit in the bottom margin of a shooting script.
    number_zone = "header (first 3 non-blank lines of each page)"
    if len(anchors) < 0.5 * len(pages):
        header_only = len(anchors)
        c2 = [page_number_candidates(p, include_footer=True) for p in pages]
        pr2, an2, tr2, ld2 = build_page_map(pages, c2)
        if len(an2) > header_only:
            cands, printed, anchors = c2, pr2, an2
            trailing_unnumbered, leading_unnumbered = tr2, ld2
            number_zone = (
                f"header + FOOTER (the header zone alone read {header_only} "
                f"page numbers; this script paginates at the foot of the page)"
            )
    segs = offset_segments(printed)

    heads, numbered_hits = find_scene_headings(pages)
    heads = filter_character_cues(heads)
    acts = find_act_labels(pages)
    first_body, last_body = body_range(printed, heads, acts)

    numbered_script = numbered_hits >= 5

    # printed positions
    for h in heads:
        lbl, val, basis = printed_of(printed, h["phys_page"], h["frac"])
        h["printed"] = lbl
        h["pos"] = val
        h["printed_basis"] = basis
    for a in acts:
        lbl, val, basis = printed_of(printed, a["phys_page"], a["frac"])
        a["printed"] = lbl
        a["pos"] = val
        a["printed_basis"] = basis

    # duplicated scene numbers (revision pages bound in twice)
    dupes = {}
    for h in heads:
        if h["scene_no"]:
            dupes.setdefault(h["scene_no"].upper(), []).append(h["printed"])
    dupes = {k: v for k, v in dupes.items() if len(v) > 1}

    # numbered scripts: how much of the scene-number sequence was recovered?
    # On a degraded scan this is the honest measure of extraction quality.
    keys = sorted(
        {k for k in (_scene_key(h["scene_no"]) for h in heads) if k is not None}
    )
    coverage = None
    if keys and len(keys) >= 5:
        hi = max(k[0] for k in keys)
        found = {k[0] for k in keys}
        coverage = {
            "sequence_runs_to": hi,
            "numbers_recovered": len(found),
            "numbers_not_recovered": sorted(set(range(1, hi + 1)) - found),
        }

    # Two physical pages printing the SAME number: unnumbered inserts, and the
    # reason the offset drifts. Taken from the READ pages only — an interpolated
    # number is an assumption about a page, never evidence of what it prints.
    from collections import Counter as _C

    read_pages = [
        (i + 1, p) for i, p in enumerate(printed) if p and p["basis"] == "READ"
    ]
    _labels = _C(p["label"] for _, p in read_pages)
    dup_printed = [
        {
            "label": lbl,
            "phys_pages": [i for i, p in read_pages if p["label"] == lbl],
        }
        for lbl in sorted(
            (k for k, n in _labels.items() if n > 1),
            key=lambda s: (int(re.sub(r"\D", "", s) or 0), s),
        )
    ]

    # ---- the denominator, and where every part of it came from ----------------
    # printed_last_read is the LAST DIRECTLY READ printed number. It is the
    # authoritative last page. Nothing after it is renumbered by inference.
    printed_last_read = read_pages[-1][1]["num"] if read_pages else None
    printed_last_read_phys = read_pages[-1][0] if read_pages else None
    first_pr = next((p for p in printed if p and p["num"] == 1), None)
    a_pages = [
        {"phys": i + 1, "label": p["label"]}
        for i, p in enumerate(printed)
        if p and p["suffix"] and p["basis"] == "READ"
    ]
    if printed_last_read:
        printed_body = printed_last_read
        denom_basis = (
            f"READ — last directly-read printed number ({printed_last_read}) "
            f"on PDF p.{printed_last_read_phys}"
        )
    else:
        printed_body = last_body - first_body + 1
        denom_basis = (
            "INFERRED — no printed number was read anywhere in this file; this is "
            "a PHYSICAL page span, not a printed one (see §1.1 rule 6)"
        )

    # ---- confidence ----------------------------------------------------------
    # The question this answers: of the denominator every percentage in the
    # report is divided by, how much was READ OFF THE PAGE and how much was
    # inferred? Anything under HIGH must be said out loud, not consumed silently.
    # Counted in PRINTED NUMBERS, not physical sheets: two sheets printing `101`
    # are one printed page number read once, and counting them twice would push
    # the ratio over 100%. `base` is every page this run claims a printed
    # identity for, so direct + interpolated + extrapolated always reconciles
    # against it and the two percentages always sum to 100.
    direct = len({p["label"] for _, p in read_pages})
    sheets_read = len(read_pages)
    interp = sum(1 for p in printed if p and p["basis"].startswith("INTERPOLATED"))
    extrap = sum(1 for p in printed if p and p["basis"] == "EXTRAPOLATED-BACK")
    base = direct + interp + extrap
    direct_pct = round(100.0 * direct / base, 1) if base else 0.0
    inferred_pct = round(100.0 * (interp + extrap) / base, 1) if base else 0.0
    if direct_pct >= CONF_HIGH:
        confidence = "high"
    elif direct_pct >= CONF_MEDIUM:
        confidence = "medium"
    else:
        confidence = "low"

    if not read_pages:
        warnings.append(
            "NO PRINTED PAGE NUMBERS ANYWHERE — not one page number was read "
            f"across {len(pages)} pages, in either the header or the footer "
            "zone. The denominator above is a PHYSICAL page count standing in "
            "for a printed one (§1.1 rule 6). Say so in the headline verdict, "
            "mark every percentage approximate, and widen every tolerance band "
            "by ±3 points before assigning a severity: transcript page breaks "
            "run long against standard pages, so the error is systematic. Do "
            "NOT report this figure as printed pages."
        )
    elif confidence != "high":
        warnings.append(
            f"{confidence.upper()}-CONFIDENCE NUMBERING — only {direct} of the "
            f"{base} page numbers this run asserts ({direct_pct}%) were READ off "
            f"the page; the remaining {inferred_pct}% is INFERRED "
            f"({interp} interpolated, {extrap} back-extrapolated, "
            f"{trailing_unnumbered} trailing pages left unnumbered). The "
            f"denominator, the offset and every page citation marked `~` below "
            f"are inferences, not measurements. Threshold for `high` is "
            f"{CONF_HIGH}% read. Say this in the report's Assumptions section "
            f"and widen every tolerance band before assigning a severity."
        )
    if trailing_unnumbered:
        warnings.append(
            f"{trailing_unnumbered} physical page(s) after PDF "
            f"p.{printed_last_read_phys} print no number and have NOT been "
            f"renumbered. They are back matter, a blank, or a publisher's page "
            f"until proven otherwise — they are not printed pages "
            f"{printed_body + 1}–{printed_body + trailing_unnumbered}."
        )
    if dup_printed:
        warnings.append(
            f"{len(dup_printed)} printed number(s) appear on more than one sheet "
            "(" + ", ".join(
                f"{d['label']}@PDF{'/'.join(str(x) for x in d['phys_pages'])}"
                for d in dup_printed[:12]
            ) + "). Printed numbering lags the physical sheets from that point on."
        )

    # scene lengths in printed pages
    positions = [h["pos"] for h in heads if h["pos"] is not None]
    lengths = []
    for i in range(len(positions) - 1):
        lengths.append(round(positions[i + 1] - positions[i], 2))
    if positions and printed_last_read:
        lengths.append(round(printed_last_read - positions[-1], 2))
    longest = max(lengths) if lengths else None
    longest_idx = lengths.index(longest) if lengths else None

    result.update(
        {
            "status": "OK",
            "numbering": {
                "printed_first_page_phys": first_pr and (printed.index(first_pr) + 1),
                "printed_last_number_read": printed_last_read,
                "printed_last_number_read_phys": printed_last_read_phys,
                "printed_body_pages": printed_body,
                "printed_body_pages_basis": denom_basis,
                "numbers_read_from": number_zone,
                # --- confidence: how much of the denominator was MEASURED ------
                "confidence": {
                    "numbers_read_directly": direct,
                    "numbers_read_directly_pct": direct_pct,
                    "physical_sheets_with_number_read": sheets_read,
                    "pages_interpolated": interp,
                    "pages_extrapolated_back": extrap,
                    "pages_inferred_total": interp + extrap,
                    "pages_inferred_pct": inferred_pct,
                    "denominator_used_for_pct": base,
                    "denominator_used_for_pct_note": (
                        "every page this run claims a printed identity for = "
                        "read + interpolated + back-extrapolated"
                    ),
                    "numbering_confidence": confidence,
                    "thresholds_pct_read": {
                        "high": CONF_HIGH,
                        "medium": CONF_MEDIUM,
                        "low": f"< {CONF_MEDIUM}",
                    },
                    "meaning": (
                        "numbers_read_directly_pct is the share of the "
                        "denominator whose printed page number was read off the "
                        "page. The remainder was inferred. Page labels prefixed "
                        "`~` in the scene and act lists are inferred."
                    ),
                },
                "leading_unnumbered_pages": leading_unnumbered,
                "trailing_unnumbered_pages": trailing_unnumbered,
                "trailing_unnumbered_note": (
                    "physical sheets after the last READ printed number. NOT "
                    "renumbered and NOT counted in printed_body_pages."
                ),
                "offset_segments": segs,
                "offset_segments_basis": "READ pages only",
                "a_pages": a_pages,
                "duplicate_printed_numbers": dup_printed,
                "drift": max(0, len(segs) - 1),
            },
            "scenes": {
                "count": len(heads),
                "numbered_script": numbered_script,
                "unique_scene_numbers": len(
                    {h["scene_no"].upper() for h in heads if h["scene_no"]}
                )
                or None,
                "duplicate_scene_numbers": dupes,
                "scene_number_coverage": coverage,
                "average_length_printed_pp": round(printed_body / len(heads), 2)
                if heads and printed_body
                else None,
                "average_length_basis": (
                    f"printed_body_pages ({printed_body}) ÷ scene count "
                    f"({len(heads)}); inherits the numbering confidence "
                    f"'{confidence}' of the denominator"
                ),
                "longest_scene_pp": longest,
                "longest_scene_at": heads[longest_idx]["printed"]
                if longest_idx is not None and longest_idx < len(heads)
                else None,
                "headings": heads,
            },
            "acts": acts,
        }
    )
    result["warnings"] = warnings
    if warnings:
        result["warning"] = "  ".join(warnings)
    return result


# ----------------------------------------------------------------------------
# 6. Rendering
# ----------------------------------------------------------------------------


def _wrap(s, width, indent):
    """Wrap a warning without pulling in textwrap's paragraph semantics."""
    words, lines, cur = s.split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return ("\n" + indent).join(lines)


def render(r, show_all_scenes=False):
    L = []
    A = L.append
    A(f"SOURCE      {r['source']}")
    A(f"EXTRACTION  {r['extraction']}")
    A(f"PAGES       {r.get('pdf_pages') or r['text_pages']} physical")
    if r["status"] == "NO TEXT LAYER":
        A("")
        A("!! NO TEXT LAYER — MEASUREMENT IMPOSSIBLE !!")
        A(f"   {r['text_layer']['chars_per_page']} non-space characters per page; "
          f"{r['text_layer']['pages_effectively_empty']} of {r['text_pages']} pages empty.")
        A("")
        for line in r["advice"].split(". "):
            if line.strip():
                A(f"   {line.strip().rstrip('.')}.")
        return "\n".join(L)

    n = r["numbering"]
    c = n["confidence"]
    A("")
    A("-- DENOMINATOR ------------------------------------------------------")
    A(f"Printed body pages     {n['printed_body_pages']}")
    A(f"   basis               {n['printed_body_pages_basis']}")
    A(f"Physical pages         {r.get('pdf_pages') or r['text_pages']}")
    A(f"Front matter           {n['leading_unnumbered_pages']} physical page(s) "
      "before the first printed number")
    A(f"Trailing unnumbered    {n['trailing_unnumbered_pages']} physical page(s) "
      "after the last printed number — reported as unnumbered, NOT renumbered")
    A("")
    A("-- CONFIDENCE -------------------------------------------------------")
    A(f"Numbers read from      {n['numbers_read_from']}")
    A(f"Page numbers asserted  {c['denominator_used_for_pct']}   "
      "(read + interpolated + back-extrapolated)")
    A(f"  READ off the page    {c['numbers_read_directly']}   "
      f"({c['numbers_read_directly_pct']}%)   <- MEASURED"
      + (f"   [on {c['physical_sheets_with_number_read']} physical sheets]"
         if c['physical_sheets_with_number_read'] != c['numbers_read_directly']
         else ""))
    A(f"  INFERRED             {c['pages_inferred_total']}   "
      f"({c['pages_inferred_pct']}%)   <- NOT MEASURED   "
      f"[{c['pages_interpolated']} interpolated, "
      f"{c['pages_extrapolated_back']} back-extrapolated]")
    A(f"NUMBERING CONFIDENCE   {c['numbering_confidence'].upper()}"
      f"   (threshold: high >= {CONF_HIGH}% read, "
      f"medium >= {CONF_MEDIUM}%, low below that)")
    A("Page labels below prefixed `~` are INFERRED, not read. `—` = unnumbered.")
    if r.get("warnings"):
        A("")
        for w in r["warnings"]:
            A("!! WARNING: " + _wrap(w, 68, "   "))
    A("")
    A("-- OFFSET -----------------------------------------------------------")
    A(f"Offset drift points    {n['drift']}   (measured from READ pages only)")
    for s in n["offset_segments"]:
        A(f"   Offset: PDF page {s['first_phys']}–{s['last_phys']} = printed "
          f"{s['first_printed']}–{s['last_printed']}   (printed = PDF − {s['offset']})")
    if n["a_pages"]:
        A(f"A-pages ({len(n['a_pages'])}): " + ", ".join(
            f"{a['label']}@PDF{a['phys']}" for a in n["a_pages"]))
    else:
        A("A-pages: none detected")
    if n.get("duplicate_printed_numbers"):
        A(f"Printed numbers used twice ({len(n['duplicate_printed_numbers'])}): "
          + ", ".join(f"{d['label']}@PDF"
                      + "/".join(str(x) for x in d["phys_pages"])
                      for d in n["duplicate_printed_numbers"][:20])
          + "   <- unnumbered inserts; they are why the offset drifts")
    else:
        A("Printed numbers used twice: none detected")
    A("")
    A("-- ACT LABELS -------------------------------------------------------")
    if r["acts"]:
        for a in r["acts"]:
            A(f"   p.{a['printed']:<6} (PDF {a['phys_page']:>3})  {a['label']}")
    else:
        A("   none printed — act boundaries must be inferred (see §1.3)")
    A("")
    A("-- SCENES -----------------------------------------------------------")
    s = r["scenes"]
    A(f"Scene headings         {s['count']}"
      + (f"   (unique scene numbers: {s['unique_scene_numbers']})"
         if s["numbered_script"] and s["unique_scene_numbers"] else ""))
    A(f"Numbered shooting script: {'yes' if s['numbered_script'] else 'no'}")
    A(f"Average scene length   {s['average_length_printed_pp']} printed pp")
    A(f"Longest scene          {s['longest_scene_pp']} pp at p.{s['longest_scene_at']}")
    cov = s.get("scene_number_coverage")
    if cov and cov["numbers_not_recovered"]:
        miss = cov["numbers_not_recovered"]
        A(f"Scene-number coverage  {cov['numbers_recovered']} of a sequence running "
          f"to {cov['sequence_runs_to']} — {len(miss)} not recoverable from this "
          f"text layer (OMITs and OCR damage): "
          + ", ".join(str(m) for m in miss[:25])
          + (" ..." if len(miss) > 25 else ""))
        A("                       -> treat scene count as a FLOOR, not a total.")
    if s["duplicate_scene_numbers"]:
        A(f"Duplicate scene numbers ({len(s['duplicate_scene_numbers'])}): "
          + ", ".join(f"{k}@{'/'.join(v)}" for k, v in
                      list(s["duplicate_scene_numbers"].items())[:12]))
    A("")
    heads = s["headings"]
    if show_all_scenes or len(heads) <= 24:
        show = heads
    else:
        show = heads[:12] + ["..."] + heads[-12:]
    for h in show:
        if h == "...":
            A(f"   ... ({len(heads) - 24} more — rerun with --scenes) ...")
            continue
        no = f"[{h['scene_no']}] " if h["scene_no"] else ""
        A(f"   p.{h['printed']:<6} (PDF {h['phys_page']:>3})  {no}{h['text']}")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "REPORT THE CONFIDENCE FIELDS. `Printed body pages` is only a\n"
            "measurement when NUMBERING CONFIDENCE is high; below that it is\n"
            "partly inferred and every percentage divided by it inherits the\n"
            "same doubt. Quote the !! WARNING lines in the report's Assumptions\n"
            "section rather than deleting them, and never promote a `~`-prefixed\n"
            "page label into a cited page number."
        ),
    )
    ap.add_argument("path", help="screenplay .pdf or pdftotext -layout .txt")
    ap.add_argument("--json", action="store_true",
                    help="machine-readable output, incl. numbering.confidence "
                         "and the top-level warnings list")
    ap.add_argument("--scenes", action="store_true",
                    help="print every scene heading (`~` = inferred page label)")
    ap.add_argument("--dump-text", metavar="OUT", help="also write the extracted text")
    args = ap.parse_args()

    if not os.path.exists(args.path):
        sys.stderr.write(f"ERROR: no such file: {args.path}\n")
        sys.exit(3)

    if args.dump_text:
        text, _ = extract_text(args.path)
        with open(args.dump_text, "w", encoding="utf-8") as fh:
            fh.write(text)

    r = analyse(args.path, args)
    if args.json:
        print(json.dumps(r, indent=2))
    else:
        print(render(r, show_all_scenes=args.scenes))
    sys.exit(2 if r["status"] == "NO TEXT LAYER" else 0)


if __name__ == "__main__":
    main()
