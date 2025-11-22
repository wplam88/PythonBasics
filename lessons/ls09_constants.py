"""Some examples of constants and functions."""

from random import choice

VOWELS: str = "aeiouy"
CONSONANTS: str = "bcdfghjklmnprstvwxz"

def random_letter(letters: str) -> str:
    """Given an alphabet, select one letter at random."""
    letter: str = choice(letters)
    return letter

def random_word() -> str:
    """Generate a random four letter word."""
    word: str
    word = random_letter(CONSONANTS)
    word = word + random_letter(VOWELS)
    word = word + random_letter(VOWELS)
    word = word + random_letter(CONSONANTS)
    return word