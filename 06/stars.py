import sys
from pathlib import Path

from utils import *

# sample input from the problem
SAMPLE = r"""
abc

a
b
c

ab
ac

a
a
a
a

b

""".strip()


def star1(puzzle: str) -> str:
    all_responses = []
    for group in puzzle.split("\n\n"):
        response_set = set()
        for response in group.split("\n"):
            for letters in response:
                response_set.add(letters)
        all_responses.append(response_set)

    return sum([len(response) for response in all_responses])


def star2(puzzle: str) -> str:
    all_responses = []
    for group in puzzle.split("\n\n"):
        responses = group.split("\n")
        shared_responses = set(responses[0])
        for response in responses[1:]:
            for letter in shared_responses.copy():
                if letter not in response:
                    shared_responses.remove(letter)

        all_responses.append(shared_responses)

    return sum([len(response) for response in all_responses])


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
    print("day 6, done")
