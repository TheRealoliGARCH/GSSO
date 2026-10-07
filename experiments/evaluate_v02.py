"""Controlled synthetic evaluation of passive versus active observation."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.gsso_v01 import Observation, simulate_active_series, simulate_passive_series
from src.gsso_v02 import (
    brier_score,
    false_warning_duration,
    roc_auc,
    total_information_cost,
    warning_lead_time,
)


def main():
    stress = [
        0.10, 0.12, 0.15, 0.18, 0.22, 0.28, 0.36,
        0.46, 0.62, 0.78, 0.92, 1.00, 1.10, 1.20
    ]
    truth = [int(s >= 0.60) for s in stress]

    passive_obs = [min(1.0, s * 0.85) for s in stress]
    passive = simulate_passive_series(passive_obs, 1.0)

    candidates = []
    for s in stress:
        candidates.append([
            Observation("macro", min(1.0, s * 0.85), 1.0),
            Observation("financial", min(1.0, s * 1.10), 0.8),
            Observation("trade", min(1.0, s * 0.70), 1.2),
        ])
    active, destinations = simulate_active_series(0.5, candidates)

    selected_costs = [
        next(o.cost for o in candidate_set if o.node == destination)
        for candidate_set, destination in zip(candidates, destinations)
    ]

    print("Metric              Passive     Active")
    print(f"AUC                 {roc_auc(truth, passive):.3f}       {roc_auc(truth, active):.3f}")
    print(f"Brier               {brier_score(truth, passive):.3f}       {brier_score(truth, active):.3f}")
    print(f"Lead time           {warning_lead_time(truth, passive)}          {warning_lead_time(truth, active)}")
    print(f"False-warning time  {false_warning_duration(truth, passive)}          {false_warning_duration(truth, active)}")
    print(f"Info cost           0.0         {total_information_cost(selected_costs):.1f}")
    print("Destinations:", destinations)


if __name__ == "__main__":
    main()
