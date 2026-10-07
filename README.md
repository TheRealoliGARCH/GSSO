# GSSO v0.1 — Passive vs Active Observation

This branch implements the first falsifiable experiment from the GSSO paper: whether active information acquisition can improve systemic-crisis warning relative to passive monitoring.

The scaffold contains:
- a minimal multilayer world representation;
- a transparent systemic-stress index;
- a passive warning baseline;
- a single active information-acquisition agent;
- information-gain-per-cost destination selection;
- unit tests;
- a reproducible synthetic experiment.

The active selection rule is j* = argmax_j IG(j)/(C(j)+epsilon).

This is deliberately not the full GSSO. It isolates the active-observation mechanism before adding a learned world model, heterogeneous agents, or MARL.

Scientific discipline:
observation != inference != prediction != causal claim != policy.

Run:
python -m unittest discover -s tests -v
python experiments/run_v01.py

Next steps:
1. Add controlled synthetic crisis-generating processes.
2. Make passive and active observers use identical model capacity.
3. Measure warning lead time, AUC, calibration, false-warning duration, and information cost.
4. Add the hybrid State-Attention world model.
5. Introduce a learned traveling agent.
6. Only then evaluate heterogeneous agents and MARL.
