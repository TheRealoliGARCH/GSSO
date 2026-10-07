"""Minimal GSSO v0.1: passive versus active observation."""
from __future__ import annotations
from dataclasses import dataclass
from math import log
from typing import Iterable, List, Sequence, Tuple

@dataclass(frozen=True)
class Node:
    name: str

@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    layer: str
    weight: float

@dataclass
class Observation:
    node: str
    value: float
    cost: float

class MultilayerWorld:
    def __init__(self, nodes: Sequence[Node], edges: Sequence[Edge]):
        self.nodes = {n.name: n for n in nodes}
        self.edges = list(edges)
    def neighbors(self, node: str) -> List[str]:
        return [e.target for e in self.edges if e.source == node]

def entropy_bernoulli(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -(p * log(p) + (1.0 - p) * log(1.0 - p))

def information_gain(prior: float, posterior: float) -> float:
    return entropy_bernoulli(prior) - entropy_bernoulli(posterior)

def information_value(prior: float, posterior: float, acquisition_cost: float, epsilon: float = 1e-12) -> float:
    if acquisition_cost < 0:
        raise ValueError("acquisition_cost must be non-negative")
    return information_gain(prior, posterior) / (acquisition_cost + epsilon)

def select_destination(prior: float, candidates: Sequence[Observation]) -> Observation:
    if not candidates:
        raise ValueError("at least one candidate is required")
    return max(candidates, key=lambda x: information_value(prior, x.value, x.cost))

def stress_index(indicators: Iterable[float], weights: Iterable[float]) -> float:
    values, ws = list(indicators), list(weights)
    if len(values) != len(ws) or not values:
        raise ValueError("indicators and weights must have equal non-zero length")
    if any(w < 0 for w in ws) or sum(ws) <= 0:
        raise ValueError("weights must be non-negative with positive sum")
    total = sum(ws)
    return sum(x * w / total for x, w in zip(values, ws))

def crisis_probability(stress: float, threshold: float = 1.0) -> float:
    if threshold <= 0:
        raise ValueError("threshold must be positive")
    return max(0.0, min(1.0, stress / threshold))

def simulate_passive_series(stress_series: Sequence[float], threshold: float) -> List[float]:
    return [crisis_probability(s, threshold) for s in stress_series]

def simulate_active_series(prior: float, candidates_by_t: Sequence[Sequence[Observation]]) -> Tuple[List[float], List[str]]:
    probabilities, destinations = [], []
    current = prior
    for candidates in candidates_by_t:
        selected = select_destination(current, candidates)
        current = selected.value
        destinations.append(selected.node)
        probabilities.append(current)
    return probabilities, destinations
