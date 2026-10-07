"""Stress-test the v0.2 evaluation across controlled observation scenarios."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.gsso_v01 import Observation, simulate_active_series, simulate_passive_series
from src.gsso_v02 import brier_score, roc_auc, warning_lead_time
from src.gsso_v03 import scenario_summary


STRESS = [0.10, 0.12, 0.15, 0.18, 0.22, 0.28, 0.36, 0.46, 0.62, 0.78, 0.92, 1.00, 1.10, 1.20]
TRUTH = [int(s >= 0.60) for s in STRESS]


def evaluate(financial_multiplier: float, financial_cost: float):
    passive_obs = [min(1.0, s * 0.85) for s in STRESS]
    passive = simulate_passive_series(passive_obs, 1.0)

    candidates = []
    for s in STRESS:
        candidates.append([
            Observation("macro", min(1.0, s * 0.85), 1.0),
            Observation("financial", min(1.0, s * financial_multiplier), financial_cost),
            Observation("trade", min(1.0, s * 0.70), 1.2),
        ])

    active, _ = simulate_active_series(0.5, candidates)
    return {
        "passive_auc": roc_auc(TRUTH, passive),
        "active_auc": roc_auc(TRUTH, active),
        "passive_brier": brier_score(TRUTH, passive),
        "active_brier": brier_score(TRUTH, active),
        "passive_lead": warning_lead_time(TRUTH, passive) or 0,
        "active_lead": warning_lead_time(TRUTH, active) or 0,
    }


def main():
    scenarios = {
        "weak_signal": (0.95, 0.8),
        "baseline": (1.10, 0.8),
        "strong_signal": (1.30, 0.8),
        "expensive_signal": (1.30, 2.0),
    }

    print("Scenario          AUC Δ     Brier Δ    Lead Δ")
    for name, (multiplier, cost) in scenarios.items():
        metrics = evaluate(multiplier, cost)
        auc = scenario_summary([metrics["passive_auc"]], [metrics["active_auc"]])
        brier = scenario_summary([metrics["passive_brier"]], [metrics["active_brier"]])
        lead = scenario_summary([metrics["passive_lead"]], [metrics["active_lead"]])
        print(
            f"{name:17s} {auc['active_minus_baseline']:+.3f}"
            f"      {brier['active_minus_baseline']:+.3f}"
            f"      {lead['active_minus_baseline']:+.0f}"
        )


if __name__ == "__main__":
    main()
