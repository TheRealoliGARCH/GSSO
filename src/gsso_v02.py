"""GSSO v0.2 evaluation utilities for controlled synthetic experiments."""
from __future__ import annotations
from typing import Iterable, Sequence

def brier_score(y_true: Sequence[int], probabilities: Sequence[float]) -> float:
    if len(y_true) != len(probabilities) or not y_true:
        raise ValueError("inputs must have equal non-zero length")
    if any(p < 0.0 or p > 1.0 for p in probabilities):
        raise ValueError("probabilities must lie in [0, 1]")
    return sum((p - y) ** 2 for y, p in zip(y_true, probabilities)) / len(y_true)

def roc_auc(y_true: Sequence[int], scores: Sequence[float]) -> float:
    if len(y_true) != len(scores) or not y_true:
        raise ValueError("inputs must have equal non-zero length")
    positives = sum(y_true)
    negatives = len(y_true) - positives
    if positives == 0 or negatives == 0:
        raise ValueError("AUC requires both positive and negative cases")
    order = sorted(range(len(scores)), key=lambda i: scores[i])
    rank_sum = 0.0
    i = 0
    rank = 1
    while i < len(order):
        j = i + 1
        while j < len(order) and scores[order[j]] == scores[order[i]]:
            j += 1
        average_rank = (rank + rank + (j - i) - 1) / 2.0
        rank_sum += average_rank * sum(y_true[order[k]] for k in range(i, j))
        rank += j - i
        i = j
    return (rank_sum - positives * (positives + 1) / 2.0) / (positives * negatives)

def warning_lead_time(y_true: Sequence[int], probabilities: Sequence[float], threshold: float = 0.5) -> int | None:
    if len(y_true) != len(probabilities) or not y_true:
        raise ValueError("inputs must have equal non-zero length")
    crisis = next((i for i, y in enumerate(y_true) if y == 1), None)
    if crisis is None:
        return None
    warning = next((i for i, p in enumerate(probabilities[:crisis + 1]) if p >= threshold), None)
    return None if warning is None else crisis - warning

def false_warning_duration(y_true: Sequence[int], probabilities: Sequence[float], threshold: float = 0.5) -> int:
    if len(y_true) != len(probabilities) or not y_true:
        raise ValueError("inputs must have equal non-zero length")
    return sum(1 for y, p in zip(y_true, probabilities) if y == 0 and p >= threshold)

def total_information_cost(costs: Iterable[float]) -> float:
    values = list(costs)
    if any(c < 0 for c in values):
        raise ValueError("costs must be non-negative")
    return sum(values)
