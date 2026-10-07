"""GSSO v0.3 helpers for repeated controlled evaluations."""
from __future__ import annotations
from statistics import mean
from typing import Callable, Sequence


def mean_metric(values: Sequence[float]) -> float:
    if not values:
        raise ValueError("values must be non-empty")
    return mean(values)


def paired_difference(baseline: Sequence[float], treatment: Sequence[float]) -> float:
    if len(baseline) != len(treatment) or not baseline:
        raise ValueError("inputs must have equal non-zero length")
    return mean(treatment[i] - baseline[i] for i in range(len(baseline)))


def scenario_summary(
    baseline_metrics: Sequence[float],
    active_metrics: Sequence[float],
) -> dict[str, float]:
    if len(baseline_metrics) != len(active_metrics) or not baseline_metrics:
        raise ValueError("inputs must have equal non-zero length")
    return {
        "baseline_mean": mean_metric(baseline_metrics),
        "active_mean": mean_metric(active_metrics),
        "active_minus_baseline": paired_difference(
            baseline_metrics, active_metrics
        ),
    }


def evaluate_scenarios(
    scenarios: Sequence[str],
    evaluator: Callable[[str], tuple[float, float]],
) -> dict[str, dict[str, float]]:
    if not scenarios:
        raise ValueError("scenarios must be non-empty")
    return {
        name: scenario_summary(
            [evaluator(name)[0]], [evaluator(name)[1]]
        )
        for name in scenarios
    }
