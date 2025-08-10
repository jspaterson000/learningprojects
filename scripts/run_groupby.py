import json
import os
from src.basics import csv_groupby

if __name__ == "__main__":
    here = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(here, "data", "jobs.csv")
    res = csv_groupby(path)
    print(json.dumps(res, indent=2))
