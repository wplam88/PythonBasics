"""This program..."""

__author__ = "Will Lam lamwillp88@gmail.com"

#Part 1: is_tar
#Function that returns True if str is made of "t" followed by any number of "a" and ends in "r"
def main() -> None:
    print(is_tar("tar"))
    print(boot("tarheels!!!", 3, 7))
    print(sum_inputs())
    print(strip("   tarheel   ", "left"))
    print(strip("   tarheel   ", "right"))
    
def is_tar(word: str) -> bool:
    if word[0] != "t":
        return False
    elif word[1] != "a":
        return False
    elif word[len(word) -1] != "r":
        return False
    else:
        return True

#Part 2: boot
#Function that takes in str, int, int, removing the characters including and between the given indicies
def boot(word: str, begin_boot: int, end_boot: int) -> str:
    i: int = 0
    new_word: str = ""
    while i < len(word):
        if begin_boot <= i <= end_boot:
            pass
        else:
            new_word += word[i]
        i += 1
    return new_word

#Part 3: sum_inputs
#Function that takes in no inputs, and repeatedly prompts the user to input numbers to sum until they type -1 causing the program to stop.
def sum_inputs() -> str:
    total_sum: int = 0
    is_running: bool = True
    while is_running:
        number_input: str = input("Enter an int, -1 to sum: ")
        if int(number_input) != -1:
            total_sum += int(number_input)
        else:
            is_running = False
    return "Sum is " + str(total_sum)

#Part 4: strip
#Takes in a an "unstripped" word with leading and trailing spaces and removes them on the left or right side given the corresponding input, returning a "stripped" word.
#likely needs to make use of a while loop to keep searching through each indicie of the word, stopping when done

#CONSTANTS
REMOVE_LEFT: str = "left"
REMOVE_RIGHT: str = "right"

#Part 4: strip
#one while loop finishes completely before another begins
def strip(raw_word: str, remove_side: str) -> str:
    clean_word: str = ""
    i: int = 0
    j: int = 0

    if remove_side == REMOVE_LEFT:
        while i < len(raw_word) and raw_word[i] == " ":
            i += 1

        while i < len(raw_word):
            clean_word += raw_word[i]
            i += 1

    elif remove_side == REMOVE_RIGHT:
        while j < len(raw_word) and raw_word[j] == " ":
            clean_word += raw_word[j]
            j += 1
        
        while j < len(raw_word) and raw_word[j] != " ":
            clean_word += raw_word[j]
            j += 1

    return clean_word

if __name__ == "__main__":
    main()


