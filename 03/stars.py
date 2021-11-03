import sys
from pathlib import Path

from utils import *

# sample input from the problem
SAMPLE = r"""
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#

""".strip()


def count_trees(tree_map: List[str], vert_update: int, horiz_update: int) -> int:
    access_idx = (0, 0)  # row, col
    tree_count = 0
    while access_idx[0] < len(tree_map):
        if tree_map[access_idx[0]][access_idx[1]] == "#":
            tree_count += 1
        access_idx = (
            access_idx[0] + vert_update,
            (access_idx[1] + horiz_update) % len(tree_map[0]),
        )
    return tree_count


def star1(puzzle: str) -> str:
    tree_map = puzzle.split("\n")
    return count_trees(tree_map, 1, 3)


def star2(puzzle: str) -> str:
    tree_map = puzzle.split("\n")
    return (
        count_trees(tree_map, 1, 1)
        * count_trees(tree_map, 1, 3)
        * count_trees(tree_map, 1, 5)
        * count_trees(tree_map, 1, 7)
        * count_trees(tree_map, 2, 1)
    )


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
    print("day 03, done")
