"""This program tests my replications of common idioms to understand the functionality behind them."""

__author__ = "Will Lam lamwillp88@gmail.com"

from exercises.ex05.utils import count
from typing import List

# count TESTS

# edge cases
def test_count_none() -> None:
    """Test counting no instances of the needle in the haystack."""
    assert count([1, 1, 0, 1, 20, 100], 7) == 0

# use cases
def test_count_one() -> None:
    """Test counting a single instance of the needle in the haystack."""
    assert count([1, 1, 0, 1, 20, 100], 0) == 1

def test_count_multiple() -> None:
    """Test counting multiple instances of the needle in the haystack."""
    assert count([1, 1, 0, 1, 20, 100], 1) == 3
