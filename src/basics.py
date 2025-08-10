from __future__ import annotations
from collections import Counter, deque
from csv import DictReader
from statistics import mean
from typing import Iterable, Sequence, Dict, List, Set, Any


def modes(xs: Sequence[int]) -> Set[int]:
    """
    Return the set of modal values (most frequent) in xs.
    Empty input -> empty set.
    """
    if not xs:
        return set()
    counts = Counter(xs)
    if not counts:
        return set()
    max_freq = max(counts.values())
    return {x for x, c in counts.items() if c == max_freq}


def rolling_mean(xs: Sequence[float], k: int) -> List[float]:
    """
    Compute rolling average over window size k in O(n) time.
    Returns an empty list if k > len(xs). Raises ValueError if k <= 0.
    """
    n = len(xs)
    if k <= 0:
        raise ValueError("k must be a positive integer")
    if k > n:
        return []
    out: List[float] = []
    window_sum = 0.0
    q = deque()  # store last k items
    for x in xs:
        q.append(float(x))
        window_sum += float(x)
        if len(q) > k:
            window_sum -= q.popleft()
        if len(q) == k:
            out.append(window_sum / k)
    return out


def csv_groupby(path: str) -> Dict[str, Dict[str, float]]:
    """
    Read jobs csv with columns: job_id,suburb,travel_km,duration_min
    Returns dict: suburb -> {count, mean_km, mean_duration}
    """
    buckets: Dict[str, Dict[str, Any]] = {}
    with open(path, newline="", encoding="utf-8") as f:
        reader = DictReader(f)
        for row in reader:
            suburb = row["suburb"].strip()
            km = float(row["travel_km"])
            dur = float(row["duration_min"])
            b = buckets.setdefault(suburb, {"kms": [], "durs": []})
            b["kms"].append(km)
            b["durs"].append(dur)
    result: Dict[str, Dict[str, float]] = {}
    for suburb, vals in buckets.items():
        result[suburb] = {
            "count": float(len(vals["kms"])),
            "mean_km": mean(vals["kms"]) if vals["kms"] else 0.0,
            "mean_duration": mean(vals["durs"]) if vals["durs"] else 0.0,
        }
    return result


def business_fizzbuzz(n: int) -> List[Any]:
    """
    For each integer 1..n inclusive:
    - "ETA" if divisible by 2
    - "RISK" if divisible by 3
    - "ETARISK" if divisible by 2 and 3
    - otherwise the number
    Returns a list without printing.
    """
    out: List[Any] = []
    for i in range(1, n + 1):
        two = (i % 2 == 0)
        three = (i % 3 == 0)
        if two and three:
            out.append("ETARISK")
        elif two:
            out.append("ETA")
        elif three:
            out.append("RISK")
        else:
            out.append(i)
    return out
