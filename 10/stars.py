import sys
from functools import lru_cache
from pathlib import Path

from utils import *

# sample input from the problem
SAMPLE = r"""
16
10
15
5
1
11
7
19
6
12
4

""".strip()


def star1(puzzle: str) -> str:
    joltages = [0] + [int(x) for x in puzzle.split()]
    joltages.sort()
    differences = [x - y for (x, y) in zip(joltages[1:] + [joltages[-1] + 3], joltages)]
    return differences.count(3) * differences.count(1)


def star2(puzzle: str) -> str:
    joltages = [int(x) for x in puzzle.split()]
    joltages.sort()

    @lru_cache(maxsize=None)
    def count_configurations(joltage_index: int, current_joltage: int) -> int:
        if joltage_index >= len(joltages) - 2:
            return 1
        accum = 0
        accum += count_configurations(joltage_index + 1, joltages[joltage_index])
        if joltages[joltage_index + 1] < current_joltage + 4:
            accum += count_configurations(
                joltage_index + 2, joltages[joltage_index + 1]
            )
        if len(joltages) > 2 and joltages[joltage_index + 2] < current_joltage + 4:
            accum += count_configurations(
                joltage_index + 3, joltages[joltage_index + 2]
            )
        return accum

    return count_configurations(0, 0)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# toggle to switch which function is run
WHICHSTAR = star2
INPUT_FILE = str(Path.cwd()) + "/input.txt"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


if __name__ == "__main__":
    if len(sys.argv) == 1:  # we're running on the example input
        print(f"\n\n {WHICHSTAR(SAMPLE)} \n\n")
    else:  # otherwise, get the input
        with open(INPUT_FILE) as puzzle_input:
            print(f"\n\n {WHICHSTAR(puzzle_input.read().strip())} \n\n")
    print("day 10, done")
