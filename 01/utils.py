from typing import List

import regex as re


# ~~~~~~~~ parsing ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def parse_ints(multiline_string: str) -> List[int]:
    return [
        int(number_string)
        for number_string in re.findall(r"-?\d+", multiline_string.strip())
    ]


def parse_list_of_ints(multiline_string: str) -> List[int]:
    cleaned_input = multiline_string.strip().split("\n")
    return [int(number_string) for number_string in cleaned_input]


def split_by_lines_and_then_spaces(multiline_string: str) -> List[List[str]]:
    cleaned_input = multiline_string.strip().split("\n")
    return [line.split(" ") for line in cleaned_input]


# ~~~~~~~~  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
