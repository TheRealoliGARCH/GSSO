# GSSO v0.2 — Controlled Evaluation

This repository implements the first falsifiable experiments from the GSSO paper: whether active information acquisition can improve systemic-crisis warning relative to passive monitoring.

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

This is deliberately not the full GSSO. It isolates the active-observation mechanism before adding a learned world model, heterogeneous agents, or MARL.

## v0.2

The controlled evaluation layer adds:
- Brier score;
- ROC AUC;
- warning lead time;
- false-warning duration;
- total information-acquisition cost;
- a controlled synthetic crisis-generating process;
- a reproducible passive-versus-active evaluation.

The comparison is deliberately capacity-controlled at this stage: both observers operate on the same synthetic environment, while the active observer may choose among alternative observations with explicit costs.

## Scientific discipline

observation != inference != prediction != causal claim != policy

The v0.2 experiment is a controlled computational experiment, not evidence of real-world crisis-prediction performance.

## Run

```bash
python -m unittest discover -s tests -v
python experiments/run_v01.py
python experiments/evaluate_v02.py
```

## Roadmap

1. Add controlled synthetic crisis-generating processes.
2. Make passive and active observers use identical model capacity.
3. Measure warning lead time, AUC, calibration, false-warning duration, and information cost.
4. Add the hybrid State-Attention world model.
5. Introduce a learned traveling agent.
6. Only then evaluate heterogeneous agents and MARL.
