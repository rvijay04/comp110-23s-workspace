"""EX02 - One Shot Wordle - Loops!"""

__author__ = "730555483"

secret_word = str("python")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001f7E8"
length_of_word: str = str(len(secret_word))
empty_string = str("")
i: int = 0
j: int = 0


current_word: str = input(f"What is your {length_of_word}-letter guess? ")
while len(current_word) != len(secret_word):
    current_word = input(f"That was not {length_of_word}-letters! Try again: ")
if len(current_word) == len(secret_word):
    while i < len(secret_word):
        if current_word[i] == secret_word[i]:
            empty_string = empty_string + GREEN_BOX
        else:
            correct: bool = False
            j = 0
            while correct is not True and j < len(secret_word):
                if secret_word[j] == current_word[i]:
                    correct = True
                j = j + 1
            if correct is True:
                empty_string = empty_string + YELLOW_BOX
            else:
                empty_string = empty_string + WHITE_BOX
        i = i + 1
    print(empty_string)  
    if current_word == secret_word:
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")