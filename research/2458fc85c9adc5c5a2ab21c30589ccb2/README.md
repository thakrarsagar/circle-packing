# Public-source check for four working circle packings

Round seed `2458fc85c9adc5c5a2ab21c30589ccb2` drew `reconcile-pending` at base `978d4bd925ba4ab62e5ceb2a3b3a108d3e283f1a`. This audit checks the strongest pinned working starts at N=500, 600, 700 and 800 against public information available on 22 October 2026. It does not claim a new record or settle priority over private submissions.

The repository's offline `src/reproduce.py` check passed 50 certificates and 12 frontier rows. `src/packing_task.py check` passed all 12 hash-pinned working starts. `reconcile.py` then independently loaded and exactly verified the four chosen working certificates, checked their saved hashes, and compared their rational radii with the currently printed Packomania values under the project's `AUDIT.md` practical guard.

| N | Working certified radius | Current printed radius | Exact gain over print |
| ---: | ---: | ---: | ---: |
| 500 | 0.023455596955367 | 0.023455498994 | 9.7961367 × 10⁻⁸ |
| 600 | 0.021479896578172 | 0.021479376754 | 5.19824172 × 10⁻⁷ |
| 700 | 0.019906357272343 | 0.019903642828 | 2.714444343 × 10⁻⁶ |
| 800 | 0.018638671925985 | 0.018637592286 | 1.079639985 × 10⁻⁶ |

All four gains clear the prespecified printed-table screen. `comparison.json` gives exact rational gains and certificate hashes. The published table still says its last update was 10 September 2026. Fresh copies of the [table](https://packomania.com/csq/) and [pending-request page](https://www.packomania.com/pending-requests.html) were byte-for-byte identical to the project's 20 October snapshots; the four live table rows also matched `data/records.json` directly.

## Pending evidence

The pending page lists 557 `csq` candidates submitted on 14 September for a range of 401–1000 circles. That range can include all four counts, but the page does not give per-count membership, radii or coordinates. It lists another 1,813 `csq` candidates submitted on 15 October for 501–9984, a range that can include 600, 700 and 800. Range inclusion alone is not a same-count comparison.

[Project Aletheia's 31 August finding](https://www.projectaletheia.org/findings?view=canonical) says it sent fixed candidate files for 600, 700 and 800 to the catalogue maintainer, and explicitly says they are not accepted records. On the public pages checked here, its relevant finding links a PNG illustration but no numeric radius or coordinate download. Its [research queue](https://www.projectaletheia.org/research) still awaits the maintainer's decision; the [data page](https://www.projectaletheia.org/datasets) does not expose an ART-085 file path. Those claims precede this project's 20 October work, but their relative radii cannot be ordered from the public information inspected. The source URLs, retrieval times, body hashes and search limits are in `source-audit.json`. No author or record keeper was contacted.

**Disposition:** these four working files are exact feasible improvements over the unchanged printed catalogue screen. Comparison with earlier pending files and priority remain unresolved. The current public pages do not supply an accessible numeric pending witness to check. This is a bounded search of the listed primary pages and targeted public results, not proof that no other witness exists.

## Replay and next step

From the repository root with Python 3.10 or newer, choose a fresh output path:

```sh
python3 src/reproduce.py
python3 src/packing_task.py check
python3 research/2458fc85c9adc5c5a2ab21c30589ccb2/reconcile.py ../packing-reconcile-replay.json
```

`reconcile.py` uses only the standard library and the unchanged `src/verify.py`; its output pins their hashes along with the working-start index and frozen published table. The current-table source hash is `01995a5a57f2adcf839c340b1108b7b67c69993452aaac842e88cdac2bec1707`, and the pending-page hash is `92ce2e3dd9802a85edda90ace95a1e7d81dac08297c3903bba46289cdb2a14ae`.

A reviewable next step is a per-count, dated earlier pending witness, with its construction credit and radius convention. Check it with `src/verify.py --n N`, compare exact radii under a common unit-square convention, and ask the maintainer to make the priority and acceptance decision. The published-table gains alone do not authorize a record submission. Original construction credit remains with the Packntile team at N=500 and Eckard Specht at N=600/700/800; this session contributes the source audit only.
