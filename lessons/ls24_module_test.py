"""An example of a test module in pytest."""

from lessons.ls24_module import total, fill_range, join
from typing import List

# total TESTS

def test_total_empty() -> None:
    """Total of empty list should be 0"""
    assert total([]) == 0.0


def test_total_single_item() -> None:
    """Total of a list with a single item should be the same number as the item contained within the list"""
    assert total([110.0]) == 110.0


def test_total_many_items() -> None:
    """Total of a list with many items, should return the sum of all 3 items"""
    assert total([1.0, 2.0, 3.0, 4.0]) == 10.0

# join TESTS

# edge cases
def test_join_no_item() -> None:
    """Join a list of many ints, returning a string of numbers with a delimiter"""
    assert join([], ", ") == ""


def test_join_single_item() -> None:
    """Join a list of many ints, returning a string of numbers with a delimiter"""
    assert join([1], "-") == "1"


def test_join_no_delimiter() -> None:
    """Join a list with no delimeter"""
    assert join([1, 2, 3], "") == "123"

# use cases
def test_join_two_items() -> None:
    """Join a list of many ints, returning a string of numbers with a delimiter"""
    assert join([1, 2], ", ") == "1, 2"


def test_join_many_items() -> None:
    """Join a list of many ints, returning a string of numbers with a delimiter"""
    assert join([1, 2, 3], "-") == "1-2-3"



# fill_range TESTS

# use cases

def test_fill_range_use_case_0() -> None:
    min: int = 1
    max: int = 3
    expected_result: List[int] = [1, 2, 3]
    assert fill_range(min, max) == expected_result


def test_fill_range_use_case_1() -> None:
    min: int = 100
    max: int = 101
    expected_result: List[int] = [100, 101]
    assert fill_range(min, max) == expected_result

# edge cases

def test_fill_range_edge_case_2() -> None:
    min: int = 3
    max: int = 1
    expected_result: List[int] = []
    assert fill_range(min, max) == expected_result


def test_fill_range_edge_case_1() -> None:
    min: int = 1
    max: int = 1
    expected_result: List[int] = [1]
    assert fill_range(min, max) == expected_result