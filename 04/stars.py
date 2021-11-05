import re
import sys
from pathlib import Path

from utils import *

# sample input from the problem
SAMPLE = r"""
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in

""".strip()


def star1(puzzle: str) -> int:
    passports = [
        dict([entry.split(":") for entry in passport.split()])
        for passport in puzzle.split("\n\n")
    ]
    count = 0
    for passport in passports:
        try:  # if these keys don't exist python raises a KeyError
            passport["byr"]
            passport["iyr"]
            passport["eyr"]
            passport["hgt"]
            passport["hcl"]
            passport["ecl"]
            passport["pid"]
            count += 1
        except KeyError:
            pass
    return count


def validate_byr(birth_year: str) -> bool:
    """byr (Birth Year) - four digits; at least 1920 and at most 2002."""
    return len(birth_year) == 4 and int(birth_year) >= 1920 and int(birth_year) <= 2002


def validate_iyr(issue_year: str) -> bool:
    """iyr (Issue Year) - four digits; at least 2010 and at most 2020."""
    return len(issue_year) == 4 and int(issue_year) >= 2010 and int(issue_year) <= 2020


def validate_eyr(expiration_year: str) -> bool:
    """eyr (Expiration Year) - four digits; at least 2020 and at most 2030."""
    return (
        len(expiration_year) == 4
        and int(expiration_year) >= 2020
        and int(expiration_year) <= 2030
    )


def validate_hgt(height: str) -> bool:
    """
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    """
    maybe_number = re.findall(r"^[0-9]+", height)
    if len(maybe_number) != 1:
        return False
    number = int(maybe_number[0])

    maybe_unit = re.findall(r"cm$|in$", height)
    if len(maybe_unit) != 1:
        return False
    unit = maybe_unit[0]

    if unit == "cm":
        return 150 <= number <= 193
    return 59 <= number <= 76


def validate_hcl(hair_color: str) -> bool:
    """hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f."""
    return len(re.findall(r"^#[a-f0-9]{6}$", hair_color)) == 1


def validate_ecl(eye_color: str) -> bool:
    """ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth."""
    return eye_color in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def validate_pid(passport_id: str) -> bool:
    """pid (Passport ID) - a nine-digit number, including leading zeroes."""
    return len(re.findall(r"^[0-9]{9}$", passport_id)) == 1


def star2(puzzle: str) -> int:
    passports = [
        dict([entry.split(":") for entry in passport.split()])
        for passport in puzzle.split("\n\n")
    ]
    count = 0
    for passport in passports:
        try:
            if (
                validate_byr(passport["byr"])
                and validate_iyr(passport["iyr"])
                and validate_eyr(passport["eyr"])
                and validate_hgt(passport["hgt"])
                and validate_hcl(passport["hcl"])
                and validate_ecl(passport["ecl"])
                and validate_pid(passport["pid"])
            ):
                count += 1
        except KeyError:
            pass
    return count


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
    print("day 4, done")
