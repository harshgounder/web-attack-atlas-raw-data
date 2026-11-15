# web-attack-atlas-raw-data

<p align="center">
  <b>The raw-data and source-registry layer of <a href="https://github.com/harshgounder/web-attack-atlas">web-attack-atlas</a>.</b><br/>
  Every aggregator, dataset, archive, awesome-list, paper hub and platform that holds<br/>
  evidence about web attacks, exploits, vulnerabilities and breaches. Linked, classified, coverage-counted.
</p>

<p align="center">
  <img alt="sources" src="https://img.shields.io/badge/registry%20entries-see%20ledger-8a2be2?style=flat-square"/>
  <img alt="license" src="https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square"/>
</p>

---

## The role in the system

The atlas system currently has five layers, joined by `entry_id`:

| repo | owns |
|---|---|
| [web-attack-atlas](https://github.com/harshgounder/web-attack-atlas) | atoms, patterns, preconditions, oracles, chains, counters |
| [ai-web-arsenal](https://github.com/harshgounder/ai-web-arsenal) | tools, install, drivers, MCP wiring |
| [web-attack-driver](https://github.com/harshgounder/web-attack-driver) | executor/critic loop |
| [web-attack-labs](https://github.com/harshgounder/web-attack-labs) | one lab per pattern |
| [web-attack-ledger](https://github.com/harshgounder/web-attack-ledger) | append-only memory of findings and failures |
| **web-attack-atlas-raw-data** (this repo) | **where the evidence lives: sources, links, provenance, coverage** |
| web-attack-corpus | reserved future name: raw record ingest, if some source ever needs local mirroring |

The atlas says what to think and try. The arsenal says what to run.
This repo says **where every fact about every attack came from, and what we have not read yet**.

## Why links, not raw dumps

Raw dumps of all recorded vulnerability history are millions of records. Cloning them
into git would fork data that already has authoritative homes. So this repo holds:

1. **registry entries**: one YAML file per source, classified, with access method and refresh cadence
2. **coverage ledger**: what has been ingested/indexed from each source, and what remains
3. **derived indexes only**: small normalised extracts where a source has no stable API, always with provenance

Raw stays upstream. This repo never forks a million-record database into git.

## Registry entry format

```yaml
id: nvd
name: National Vulnerability Database
kind: aggregator            # aggregator | exploit-archive | dataset | awesome-list | paper-hub | breach-db | vendor-advisory | writeup-hub | platform-doc
scope: universal            # universal | stack:cms | stack:framework:express | auth:oauth ...
access:
  api: https://services.nvd.nist.gov/rest/json/cves/2.0
  bulk: https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-modified.json.gz
  license: public-domain
atlas_link:
  atoms: [A08, A11]
  control_classes: [C10]
coverage:
  status: registered        # registered | partial | full
  notes: ...
```

## Layout

```
sources/          one YAML per source, grouped by kind
coverage/         per-source coverage ledger
derived/          small normalised extracts with provenance headers
scripts/          validation, coverage reports, dedupe
```

## Contributing

A source without an access method is not an entry. A coverage claim without a
count is not coverage. Same gate discipline as the atlas, applied to raw data.

## License

MIT.
