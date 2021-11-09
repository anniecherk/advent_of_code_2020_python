import sys
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Tuple

from utils import *

# sample input from the problem
SAMPLE = r"""
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
""".strip()


class Command(Enum):
    NOP = "nop"
    ACC = "acc"
    JMP = "jmp"


@dataclass
class Instruction:
    command: Command
    amount: int


def parse(puzzle: str) -> List[Instruction]:
    program = []
    for line in puzzle.split("\n"):
        instruction = line.split()
        program.append(Instruction(Command(instruction[0]), int(instruction[1])))
    return program


def run_program(program: List[Instruction]) -> Tuple[int, bool]:
    """
    Runs the program, avoiding infinite loops.
    Returns a tuple: the value of the global accumulator, and a flag which is True
    if the program exited early because there was an infinite loop
    """
    seen = [False] * len(program)
    pc = 0
    acc = 0
    while pc < len(program) and not seen[pc]:
        seen[pc] = True
        instruction = program[pc]
        if instruction.command == Command.NOP:
            pc += 1
        elif instruction.command == Command.ACC:
            acc += instruction.amount
            pc += 1
        else:
            pc += instruction.amount
    return (acc, pc != len(program))


def star1(puzzle: str) -> str:
    program = parse(puzzle)
    return run_program(program)[0]


def star2(puzzle: str) -> str:
    program = parse(puzzle)
    for pos, instruction in enumerate(program):
        if instruction.command.ACC:
            continue
        patch = Command.JMP if instruction.command == Command.NOP else Command.NOP
        patched_program = program.copy()
        patched_program[pos] = Instruction(patch, instruction.amount)
        result = run_program(patched_program)
        if not result[1]:
            return result[0]
    return "oh no didn't find it"


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
    print("day 8, done")
