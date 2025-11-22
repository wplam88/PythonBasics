"""Examples from Sequences"""

from typing import Tuple, List

Color = Tuple[int, int, int]

def main() -> None:
    a_list: List[int] = [110, 210, 211, 301, 311]
    print(a_list)

    # Access items using subscription notation:
    i: int = 0 
    while i < len(a_list):
        print(a_list[i])
        i += 1
    
    names: List[str] = ["William" , "Preston"]
    print(names)

    names.append("Lam")
    print(names)

def brighter(a_color: Color) -> Color:
    """Return a new tuple that is slightly brighter"""
    red: int = int(a_color[0] * 1.1)
    blue: int = int(a_color[1] * 1.1)
    green: int = int(a_color[2] * 1.1)
    return (red, blue, green)

if __name__ == "__main__":
    main()
