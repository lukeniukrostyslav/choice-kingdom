from __future__ import annotations

import argparse
from pathlib import Path
from time import perf_counter

from runtime.engine import DecisionEngine
from runtime.state import GameState

ROOT = Path(__file__).resolve().parents[1]
ITERATIONS = 250
MAX_SECONDS = 5.0


def benchmark(iterations: int = ITERATIONS) -> float:
    engine = DecisionEngine(ROOT)
    started = perf_counter()
    for index in range(iterations):
        state = GameState.fresh(f"perf-{index}")
        engine.execute(state, "E01", "E01-A")
        state.snapshot()
        engine.available(state)
    return perf_counter() - started


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--iterations", type=int, default=ITERATIONS)
    parser.add_argument("--max-seconds", type=float, default=MAX_SECONDS)
    args = parser.parse_args()
    if args.iterations < 1 or args.max_seconds <= 0:
        raise SystemExit("invalid benchmark parameters")
    elapsed = benchmark(args.iterations)
    print(f"block18_iterations={args.iterations}")
    print(f"block18_elapsed_seconds={elapsed:.6f}")
    print(f"block18_max_seconds={args.max_seconds:.6f}")
    if elapsed > args.max_seconds:
        raise SystemExit(
            f"Block 18 performance budget exceeded: {elapsed:.6f}s > {args.max_seconds:.6f}s"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
