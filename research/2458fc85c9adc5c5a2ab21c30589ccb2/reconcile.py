"""Exact published-table comparison for four pinned working witnesses."""
import hashlib
import json
import sys
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
from verify import load_verify

COUNTS = (500, 600, 700, 800)
SEED = "2458fc85c9adc5c5a2ab21c30589ccb2"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decimal(value):
    with localcontext() as context:
        context.prec = 40
        return str(Decimal(value.numerator) / Decimal(value.denominator))


def main():
    if len(sys.argv) != 2 or Path.cwd().resolve() != ROOT:
        raise SystemExit("Run from repository root: python research/2458fc85c9adc5c5a2ab21c30589ccb2/reconcile.py OUTPUT")
    output = Path(sys.argv[1])
    if output.exists():
        raise ValueError("Output exists; preserve prior comparison")
    index = ROOT / "discover/working-starts.json"
    records = ROOT / "data/records.json"
    starts = {r["n"]: r for r in json.loads(index.read_text())["rows"]}
    published = {r["n"]: r for r in json.loads(records.read_text())}
    result = {"round_seed": SEED, "base": "978d4bd925ba4ab62e5ceb2a3b3a108d3e283f1a",
              "scope": "Four pinned equal-circle working witnesses versus the frozen published Packomania table; no pending-witness comparison",
              "source_sha256": {p: sha(ROOT / p) for p in (
                  "research/2458fc85c9adc5c5a2ab21c30589ccb2/reconcile.py",
                  "src/verify.py", "discover/working-starts.json", "data/records.json")},
              "rows": []}
    for n in COUNTS:
        start, record = starts[n], published[n]
        checked = load_verify(ROOT / start["certificate"], n)
        assert checked["sha256"] == start["sha256"]
        radius = Fraction(checked["radius_exact"])
        assert radius == Fraction(start["radius_exact"])
        printed = Fraction(record["published_radius"])
        delta = radius - printed
        guard = Fraction("1e-12") + max(Fraction("1e-10"), printed * Fraction("1e-8"))
        assert delta > guard
        result["rows"].append({"n": n, "certificate": start["certificate"],
                               "certificate_sha256": checked["sha256"],
                               "construction_credit": start["construction_credit"],
                               "published_url": record["source"],
                               "published_radius": record["published_radius"],
                               "working_radius_exact": str(radius),
                               "working_radius_decimal": decimal(radius),
                               "gain_exact": str(delta), "gain_decimal": decimal(delta),
                               "practical_guard_exact": str(guard),
                               "above_published_screen": True,
                               "pending_novelty": "unresolved"})
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"verified": len(result["rows"]), "counts": list(COUNTS),
                      "all_above_published_screen": True, "pending_novelty": "unresolved"}))


if __name__ == "__main__":
    main()
