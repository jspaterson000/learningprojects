from collections import Counter, deque
from csv import DictReader
from statistics import mean
from typing import List, Set, Sequence, Hashable, Dict, Any

def modes(xs: Sequence[Hashable]) -> Set[Hashable]:
    """
    Return ALL modal values (ties allowed). Empty input -> empty set.
    Examples:
        modes([1,1,2,2,3]) -> {1,2}
        modes([]) -> set()
    """
    if not xs:
        return set()
    counts = Counter(xs)
    max_freq = max(counts.values())
    return {x for x, c in counts.items() if c == max_freq}

def rolling_mean(xs: Sequence[float], k: int) -> List[float]:
    """
    Compute a k-length moving average in O(n) time.

    Example:
        rolling_mean([1,2,3,4,5], 3) == [2.0, 3.0, 4.0]
    """
    if not isinstance(k, int) or k <= 0:
        raise ValueError("k must be a positive integer")
    n = len(xs)
    if k > n:
        return []
    out: List[float] = []
    window_sum = 0.0
    q = deque()
    for x in xs:
        x = float(x)
        q.append(x)
        window_sum += x
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
