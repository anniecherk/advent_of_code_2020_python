import sys
from collections import defaultdict
from pathlib import Path
from typing import Tuple

from utils import *

# sample input from the problem
SAMPLE = r"""
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

""".strip()


def eval_password(min_occ: int, max_occ: int, occ: str, pwd: str) -> bool:
    letters = defaultdict(int)
    for char in pwd:
        letters[char] += 1
    return (letters[occ] >= min_occ) and (letters[occ] <= max_occ)


def eval_password_2(first_occ: int, second_occ: int, occ: str, pwd: str) -> bool:
    success = 0
    try:
        if pwd[first_occ - 1] == occ:
            success += 1
        if pwd[second_occ - 1] == occ:
            success += 1
    except IndexError:
        pass
    return success == 1


def parse(entry: str) -> Tuple[int, int, str, str]:
    min_occ = parse_positive_ints(entry[0])[0]
    max_occ = parse_positive_ints(entry[0])[1]
    occ = entry[1].split(":")[0]
    pwd = entry[2]
    return (min_occ, max_occ, occ, pwd)


def validate(puzzle: str, eval_func) -> int:
    valid_pwd = 0
    for entry in split_by_lines_and_then_spaces(puzzle):
        (min_occ, max_occ, occ, pwd) = parse(entry)
        if eval_func(min_occ, max_occ, occ, pwd):
            valid_pwd += 1
    return valid_pwd


def star1(puzzle: str) -> str:
    return validate(puzzle, eval_password)


def star2(puzzle: str) -> str:
    return validate(puzzle, eval_password_2)


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
            print("Running over input.txt....")
            print(f"\n\n {WHICHSTAR(puzzle_input.read())} \n\n")
    print("day 2, done")
