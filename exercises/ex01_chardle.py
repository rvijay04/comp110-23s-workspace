"""EX01 - Chardle - a cute step toward Wordle."""

__author__ = "730555483"

num_index: int = 0
five_char: str = input("Enter a 5-character word: ")
if len(five_char) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_char: str = input("Enter a single character: ")
if len(single_char) != 1:
    print("Error: Character much be a single character.")
    exit()
print("Searching for " + single_char + " in " + five_char)
if five_char[0] == single_char:
    print(single_char + " found at index 0 ")
    num_index = num_index + 1
if five_char[1] == single_char:
    print(single_char + " found at index 1 ")
    num_index = num_index + 1
if five_char[2] == single_char:
    print(single_char + " found at index 2 ")
    num_index = num_index + 1
if five_char[3] == single_char:
    print(single_char + " found at index 3 ")
    num_index = num_index + 1
if five_char[4] == single_char:
    print(single_char + " found at index 4 ")
    num_index = num_index + 1
if num_index == 0:
    print("Error: No instances of " + single_char + " found in " + five_char)
else:
    if num_index > 1:
        print((str(num_index)) + " instances of " + single_char + " found in " + five_char)
    if num_index == 1:
        print((str(num_index)) + " instance of " + single_char + " found in " + five_char)