import sys
from pathlib import Path
from typing import List, Set, Tuple

from utils import *

# sample input from the problem
SAMPLE = r"""
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
""".strip()


def sum_of_two(nums: Set[int], goal: int) -> bool:
    for num in nums:
        soulmate = goal - num
        if soulmate in nums:
            return True
    return False


def star1(puzzle: str) -> str:
    stream = [int(x) for x in puzzle.split()]
    start_preamble = 0
    end_preamble = 24  # length preamble minus one # 4 for example # 24 for full puzzle
    preamble = set()

    for i in range(start_preamble, end_preamble + 1):
        preamble.add(stream[i])

    for i in range(end_preamble + 1, len(stream)):
        goal = stream[i]
        if not sum_of_two(preamble, goal):
            return goal
        # otherwise, advance the preamble
        preamble.remove(stream[start_preamble])
        start_preamble += 1
        end_preamble += 1
        preamble.add(stream[end_preamble])
    return "uhoh didn't find it"


def star2(puzzle: str) -> str:
    stream = [int(x) for x in puzzle.split()]

    def find_goal_run(stream, goal, index_to_add) -> Tuple[bool, List[int]]:
        if index_to_add > len(stream):
            return (False, [])

        val = stream[index_to_add]
        if val == goal:
            return (True, [val])
        if val > goal:
            return (False, [])
        result = find_goal_run(stream, goal - val, index_to_add + 1)
        if result[0]:
            return (True, [val] + result[1])
        return (False, [])

    run = None
    goal = star1(puzzle)
    for i in range(0, len(stream)):
        result = find_goal_run(stream, goal, i)
        if result[0]:
            run = result[1]
            break

    return min(run) + max(run)


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
    print("day 9, done")
