import sys
from pathlib import Path
from typing import Tuple

from utils import *

# sample input from the problem
SAMPLE = r"""
BFFFBBFRRR
""".strip()


def star1(puzzle: str) -> str:
    return max([compute_seat_id(boarding_card) for boarding_card in puzzle.split("\n")])


def compute_seat_id(boarding_card: str) -> Tuple[int, int, int]:
    row = int(
        "".join(["1" if curr_char == "B" else "0" for curr_char in boarding_card[:7]]),
        2,
    )
    col = int(
        "".join(["1" if curr_char == "R" else "0" for curr_char in boarding_card[7:]]),
        2,
    )
    seat_id = 8 * row + col
    return seat_id


def star2(puzzle: str) -> str:
    all_seat_ids = set(
        compute_seat_id(boarding_card) for boarding_card in puzzle.split("\n")
    )

    # try all seats, looking for one missing seat id surrounded by two existing ids
    for current_seat_id in range(1, 900):
        if (
            (current_seat_id in all_seat_ids)
            and (current_seat_id + 1 not in all_seat_ids)
            and (current_seat_id + 2 in all_seat_ids)
        ):
            return current_seat_id + 1

    return "uhoh, didn't find it"


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
    print("day 5, done")
