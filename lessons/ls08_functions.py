"""Example function definitions"""

def square(x: float) -> float:
    "Returns the parameter value squared"
    squared_value: float = power(x, 2)
    return squared_value


def power(x: float, exp: int) -> float:
    """Returns x raised to the exp."""
    raised_value: float= x ** exp
    return raised_value
