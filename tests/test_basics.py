import os
from src.basics import modes, rolling_mean, csv_groupby, business_fizzbuzz

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "jobs.csv")

def test_modes_basic():
    assert modes([1,1,2,2,3]) == {1,2}
    assert modes([5]) == {5}
    assert modes([]) == set()

def test_rolling_mean_basic():
    assert rolling_mean([1,2,3,4,5], 3) == [2.0, 3.0, 4.0]
    assert rolling_mean([10, 20, 30], 1) == [10.0, 20.0, 30.0]

def test_rolling_mean_edge_cases():
    assert rolling_mean([1,2], 3) == []
    try:
        rolling_mean([1,2,3], 0)
        assert False, "Expected ValueError for k=0"
    except ValueError:
        pass

def test_csv_groupby_structure():
    res = csv_groupby(DATA_PATH)
    # basic shape
    assert isinstance(res, dict) and len(res) >= 3
    # has expected keys and positive means
    for suburb, agg in res.items():
        assert {"count", "mean_km", "mean_duration"} <= set(agg.keys())
        assert agg["count"] >= 1
        assert agg["mean_km"] > 0
        assert agg["mean_duration"] > 0

def test_business_fizzbuzz():
    out = business_fizzbuzz(6)
    assert out == [1, "ETA", "RISK", "ETA", 5, "ETARISK"]

def test_modes_multiple_winners():
    data = [1, 2, 2, 3, 3, 3, 1, 1, 1]
    assert modes(data) == {1, 3}