from pathlib import Path
import sys

# Allow the experiment to be run directly from the repository root:
# python experiments/run_v01.py
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.gsso_v01 import Observation, simulate_active_series, simulate_passive_series


def main():
    stress = [0.10, 0.20, 0.35, 0.55, 0.80, 1.20]
    passive = simulate_passive_series(stress, 1.0)
    candidates = [[
        Observation("macro", min(1.0, s), 1.0),
        Observation("financial", min(1.0, s * 1.2), 0.8),
        Observation("trade", min(1.0, s * 0.8), 1.2),
    ] for s in stress]
    active, destinations = simulate_active_series(0.5, candidates)
    print("Passive:", [round(x, 3) for x in passive])
    print("Active: ", [round(x, 3) for x in active])
    print("Travel: ", destinations)


if __name__ == "__main__":
    main()
