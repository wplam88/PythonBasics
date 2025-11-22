"""An example Python module."""

from typing import List

def total(xs: List[float]) -> float:
    """total returns the sum of xs"""
    result: float = 0.0
    # for each x in xs add it to result
    for x in xs:
        result += x
    return result

def join(xs: List[int], delimiter: str) -> str:
    """join returns a a str of numbers separated by a delimter"""
    result: str = ""
    #for each x in xs append it to the previous str with -#
    #if len(xs) >= 1, dont put delimeter after
    #if final x in xs, dont put delimiter after
    for item in xs:
        if result == "": # don't put delimiter before first item
            result = str(item)
        else:
            result += delimiter + str(item)
    return result

def fill_range(min: int, max: int) -> List[int]:
    """generate a list of consecutive integers increasing between params, INCLUSIVE of those params"""
    result: List[int] = []
    # method 1 (this way is correct, but the code below makes use of a more concise for loop)
    # while min <= max:
    #     result += [min]
    #     min += 1

    # method 2 (for loop)
    for i in range(min, max + 1):
        result.append(i)
    return result

