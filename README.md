# Lesson 1 — Python Problem-Solving Warm-up

This mini-project contains:
- Clean, tested Python functions (modes, rolling mean, CSV groupby, business FizzBuzz)
- A sample dataset under `data/jobs.csv`
- Pytest tests in `tests/`

## Quickstart

```bash
# Windows PowerShell (recommended) or macOS/Linux
python -m venv .venv
# On Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# On macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
pytest -q
```

You should see tests pass. Explore `scripts/run_groupby.py` to run the CSV groupby example.

## Functions overview

- `modes(xs)` → set of the most frequent items (empty set for empty input)
- `rolling_mean(xs, k)` → O(n) rolling average using a window sum
- `csv_groupby(path)` → per-suburb summary: count, mean_km, mean_duration
- `business_fizzbuzz(n)` → list of `int` or `str` per the ETA/RISK rule

## Why rolling mean is O(n)
We keep a running sum for a sliding window and subtract the element leaving the window as we add the new element. Each item is added once and subtracted once. Constant-time per step → linear overall.
