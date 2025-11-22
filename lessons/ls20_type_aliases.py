"""Examples of type aliases."""

from typing import Tuple

Percent = float
Point3D = Tuple[float, float, float]


def main() -> None:
    print(ratio(1, 2))
    a_point: Point3D = (0.0, 1.0, 2.0)


def ratio(numer: int, denom: int) -> Percent:
    """Calculate a simple percentage."""
    return numer / denom

if __name__ == "__main__":
    main()