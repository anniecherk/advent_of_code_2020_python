import sys
from collections import defaultdict
from pathlib import Path
from typing import DefaultDict, Tuple

from utils import *

# sample input from the problem
SAMPLE = r"""
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

""".strip()


def star1(puzzle: str) -> str:
    rules = [
        re.findall(r"([0-9])*([a-z\s]+) bag", rule)
        for rule in puzzle.split("\n")
        if not "contain no other bags" in rule
    ]
    # construct the contained by lookup table
    contained_by = defaultdict(list)
    for rule in rules:
        outside_bag = rule[0][1].strip()
        for (_, bag) in rule[1:]:
            contained_by[bag.strip()].append(outside_bag)
    # compute how many bags can contain the shiny gold bag
    bags_to_check = contained_by["shiny gold"]
    seen = set()
    total_bags = 0
    while len(bags_to_check) > 0:
        current_bag = bags_to_check[0]
        if current_bag not in seen:
            total_bags += 1
            bags_to_check.extend(contained_by[current_bag])
            seen.add(current_bag)
        bags_to_check = bags_to_check[1:]
    return total_bags


def star2(puzzle: str) -> str:
    rules = [
        re.findall(r"([0-9])*([a-z\s]+) bag", rule)
        for rule in puzzle.split("\n")
        if not "contain no other bags" in rule
    ]
    # construct the lookup table for what other bags a bag contains
    contains = defaultdict(list)
    for rule in rules:
        outside_bag = rule[0][1].strip()
        contains[outside_bag].extend(
            [(int(num), color.strip()) for (num, color) in rule[1:]]
        )

    def bags_in_color(
        current_color: str, contains: DefaultDict[str, Tuple[int, str]]
    ) -> int:
        bags_to_count = contains[current_color]
        if len(bags_to_count) == 0:
            return 0
        return sum(
            [
                int(times) + int(times) * bags_in_color(color, contains)
                for (times, color) in bags_to_count
            ]
        )

    return bags_in_color("shiny gold", contains)


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
    print("day 7, done")
