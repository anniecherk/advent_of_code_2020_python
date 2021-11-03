import sys
from pathlib import Path

from utils import *

SAMPLE = r"""1721
979
366
299
675
1456

""".strip()


def star2(puzzle: str) -> str:
    ints = parse_list_of_ints(puzzle)
    seen = {}
    for elem1 in ints:
        for elem2 in ints:
            seen[elem1 + elem2] = (elem1, elem2)
    # print(seen)
    for elem in ints:
        soulmate = 2020 - elem
        if soulmate in seen:
            elem1, elem2 = seen[soulmate]
            return f" found: {seen[soulmate], elem}, {elem1*elem2*elem}"
    print("uhoh didn't find")
    return ""


def star1(puzzle: str) -> str:
    ints = parse_list_of_ints(puzzle)
    seen = set()
    for elem in ints:
        soulmate = 2020 - elem
        if soulmate in seen:
            return f" found: {elem * soulmate}"
        seen.add(elem)
    print("uhoh didn't find")
    return ""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# toggle to switch which function is run
WHICHSTAR = star2
INPUT_FILE = str(Path.cwd()) + "/input.txt"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


if __name__ == "__main__":
    whichstar = star2
    if len(sys.argv) == 1:  # we're running on the example input
        print(f"\n\n {whichstar(SAMPLE)} \n\n")
    else:  # otherwise, get the input
        with open(INPUT_FILE) as puzzle_input:
            print(f"\n\n {whichstar(puzzle_input.read())} \n\n")
    print("day 1, done")
