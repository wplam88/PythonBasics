"""Example of if-then-else statements."""

THE_ANSWER_TO_LIFE_THE_UNIVERSE_AND_EVERYTHING: int = 42

print("Guess a number...")

guess: int = int(input("Your Guess: "))

if guess == THE_ANSWER_TO_LIFE_THE_UNIVERSE_AND_EVERYTHING:
    print("Correct!")
else: 
    if guess > THE_ANSWER_TO_LIFE_THE_UNIVERSE_AND_EVERYTHING:
        print("Too High!")
    else:
        print("Too Low!")


print("Game over")
