# GSSO v0.3 — Controlled Robustness Evaluation

This repository implements controlled computational tests of the GSSO active-observation mechanism.

## v0.1

The scaffold contains:
- a minimal multilayer world representation;
- a transparent systemic-stress index;
- a passive warning baseline;
- a single active information-acquisition agent;
- information-gain-per-cost destination selection;
- unit tests;
- a reproducible synthetic experiment.

The active selection rule is:

j* = argmax_j IG(j)/(C(j)+epsilon).

This deliberately isolates the active-observation mechanism before adding a learned world model, heterogeneous agents, or MARL.

## v0.2

The controlled evaluation layer adds:
- Brier score;
- ROC AUC;
- warning lead time;
- false-warning duration;
- total information-acquisition cost;
- a controlled synthetic crisis-generating process;
- a reproducible passive-versus-active evaluation.

## v0.3

The robustness layer varies controlled observation conditions:
- weak financial signal;
- baseline financial signal;
- strong financial signal;
- expensive financial signal.

The purpose is not to establish real-world superiority. It is to determine whether the observed active-versus-passive difference is sensitive to the signal-strength and acquisition-cost assumptions.

## Scientific discipline

observation != inference != prediction != causal claim != policy

All v0.x experiments are controlled computational experiments. They are not evidence of real-world systemic-crisis prediction performance.

## Run

```bash
python -m unittest discover -s tests -v
python experiments/run_v01.py
python experiments/evaluate_v02.py
python experiments/stress_test_v03.py
```

## Roadmap

1. Controlled robustness testing.
2. Multiple independently generated crisis paths.
3. Statistical aggregation across replications.
4. Calibration and uncertainty analysis.
5. Add the hybrid State-Attention world model.
6. Introduce a learned traveling agent.
7. Only then evaluate heterogeneous agents and MARL.
