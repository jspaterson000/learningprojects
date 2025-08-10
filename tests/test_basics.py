from basics import modes, rolling_mean, csv_groupby
import os
import pytest

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "jobs.csv")

def test_modes_multiple_winners():
    data = [1, 2, 2, 3, 3, 3, 1, 1, 1]
    assert modes(data) == {1, 3}

def test_modes_empty_and_single():
    assert modes([]) == set()
    assert modes([5]) == {5}

def test_rolling_mean_happy_path():
    assert rolling_mean([1,2,3,4,5], 3) == [2.0, 3.0, 4.0]

def test_rolling_mean_edges_and_errors():
    assert rolling_mean([1,2], 3) == []
    with pytest.raises(ValueError): rolling_mean([1,2,3], 0)
    with pytest.raises(ValueError): rolling_mean([1,2,3], -1)
    with pytest.raises(ValueError): rolling_mean([1,2,3], 2.5)

def test_csv_groupby_structure():
    res = csv_groupby(os.path.abspath(DATA_PATH))
    assert isinstance(res, dict) and len(res) >= 3
    for agg in res.values():
        assert {"count", "mean_km", "mean_duration"} <= set(agg.keys())
        assert agg["count"] >= 1
        assert agg["mean_km"] > 0
        assert agg["mean_duration"] > 0
