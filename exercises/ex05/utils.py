"""This program replicates common idioms to understand the functionality behind them."""

__author__ = "Will Lam lamwillp88@gmail.com"

from typing import List

def main() -> None:
    (count([1, 1, 2, 3], 1))

def count(values: List[int], desired_value) -> int:
    desired_value_instances: int = 0
    for i in values:
        if i == desired_value:
            desired_value_instances += 1
    return(desired_value_instances)

def all(inputs: List[int], matching_value) -> bool:
    is_matching: bool = True
    for i in inputs:
        if List[i] != matching_value:
            is_matching = False
        elif List[i - 1] != matching_value:
            is_matching = False
    return is_matching

if __name__ == "__main__":
    main()