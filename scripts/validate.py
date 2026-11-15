#!/usr/bin/env python3
"""validate the registry: unique ids, required fields, url shape, coverage counts.

same gate philosophy as web-attack-atlas: if a number disagrees with this script,
the script is right. exit 1 on failure.
"""
import sys, re, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "sources"

URL_RE = re.compile(r"^https?://[a-z0-9.-]+", re.I)
REQUIRED = ("id", "name", "url")

def parse_entries(text):
    """minimal yaml reader for our own restricted subset."""
    entries, cur = [], None
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^  - ([\w][\w-]*): ?(.*)$", line)
        if m:
            if cur:
                entries.append(cur)
            cur = {m.group(1): m.group(2).strip()}
            continue
        m = re.match(r"^    ([\w][\w-]*): ?(.*)$", line)
        if m and cur is not None:
            cur[m.group(1)] = m.group(2).strip()
    if cur:
        entries.append(cur)
    return [e for e in entries if "id" in e]

def main():
    errors, all_ids = [], collections.Counter()
    per_file = {}
    for path in sorted(SRC.glob("*.yaml")):
        entries = parse_entries(path.read_text())
        per_file[path.name] = len(entries)
        for e in entries:
            all_ids[e["id"]] += 1
            for field in REQUIRED:
                if field not in e or not e[field]:
                    errors.append("%s: entry %s missing %s" % (path.name, e.get("id", "?"), field))
            if "url" in e and not URL_RE.match(e["url"]):
                errors.append("%s: entry %s bad url %s" % (path.name, e["id"], e["url"]))
    for entry_id, n in all_ids.items():
        if n > 1:
            errors.append("duplicate id %s x%d" % (entry_id, n))

    total = sum(per_file.values())
    print("registry counts:")
    for name, n in per_file.items():
        print("  %-28s %d" % (name, n))
    print("  %-28s %d" % ("TOTAL", total))
    if errors:
        print("FAILURES:")
        for e in errors:
            print("  " + e)
        sys.exit(1)
    print("registry OK")

if __name__ == "__main__":
    main()
