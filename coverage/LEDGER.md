# coverage ledger

append-only. every line records what has been registered, ingested or verified, and what remains.
counts are produced by scripts/validate.py, not by hand.

## 2026-11-15

- registry created. 10 category files under sources/.
- registered: aggregators 17, exploit-archives 11, datasets 10, awesome-lists 14, paper-hubs 15, breach-databases 6, payload-corpora 10, vendor-advisories 33, platform-trackers 30, writeup-hubs 10, auth-method-trackers 11, connector-edge-trackers 5. total: 172. counts from scripts/validate.py run of 2026-11-15.
- coverage status of every source: registered (link and access method only). zero sources reached partial or full ingest.
- next: wave R-ING-01, vendor-advisories full enumeration (all cnas from cve.org/partners), then per-source ingest scripts.
