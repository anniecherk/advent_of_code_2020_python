import sys
from pathlib import Path

from utils import *

# sample input from the problem
SAMPLE = r"""
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL

""".strip()


def update_star1(row: int, col: int, room: List[str]) -> str:
    filled = 0
    if row != 0:  # top three neighbors
        filled += 1 if room[row - 1][col] == "#" else 0
        if col != 0:
            filled += 1 if room[row - 1][col - 1] == "#" else 0
        if col != len(room[0]) - 1:
            filled += 1 if room[row - 1][col + 1] == "#" else 0
    if row != len(room) - 1:  # bottom three neighbors
        filled += 1 if room[row + 1][col] == "#" else 0
        if col != 0:
            filled += 1 if room[row + 1][col - 1] == "#" else 0
        if col != len(room[0]) - 1:
            filled += 1 if room[row + 1][col + 1] == "#" else 0
    if col != 0:  # left three neighbors
        filled += 1 if room[row][col - 1] == "#" else 0
    if col != len(room[0]) - 1:  # right three neighbors
        filled += 1 if room[row][col + 1] == "#" else 0

    # update rules:
    """
    If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.
    """
    if room[row][col] == "L":
        if filled == 0:
            return "#"
    elif room[row][col] == "#":
        if filled >= 4:
            return "L"
    return room[row][col]



def count_empty_seats(room: List[str]) -> int:
    return sum([1 for x in "".join(room) if x == "#"])


def fixed_point(room: List[str], new_room: List[str], update_func) -> List[str]:
    while room != new_room:
        room = new_room
        new_room = []
        for row_idx, row in enumerate(room):
            new_row = []
            for col_idx, _ in enumerate(row):
                new_row.append(update_func(row_idx, col_idx, room))
            new_room.append("".join(new_row))
    return room


def star1(puzzle: str) -> str:
    room = []
    new_room = puzzle.split("\n")
    stable_room = fixed_point(room, new_room, update_star1)
    return count_empty_seats(stable_room)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# toggle to switch which function is run
WHICHSTAR = star1
INPUT_FILE = str(Path.cwd()) + "/input.txt"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


if __name__ == "__main__":
    if len(sys.argv) == 1:  # we're running on the example input
        print(f"\n\n {WHICHSTAR(SAMPLE)} \n\n")
    else:  # otherwise, get the input
        with open(INPUT_FILE) as puzzle_input:
            print(f"\n\n {WHICHSTAR(puzzle_input.read().strip())} \n\n")
    print("day 11, done")
