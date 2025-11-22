"""A program that has all the answers! An 8ball game."""

from random import randint


def main() -> None:
    """Entrypoint function into game"""
    is_playing: bool = True
    while is_playing:
        input("Ask a yes/no question: ")
        random_value: int = randint (0, 3)
        print(response(random_value))
        is_playing = input("Continue? yes/no: ") == "yes"
    print("Have a great day!")


def response(n: int) -> str:
    if n == 0:
        return "Definitely, yes!"
    else:
        if n == 1:
            return "Ask again later."
        else:
            return "Unlikely."

# Python Idiom (Convention) for a runnable Python module        
if __name__ == "__main__":
    main()