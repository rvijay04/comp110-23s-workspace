"""EX03 - Structured Wordle"""
__author__ = "730555483"


def contains_char(string_one: str, single_char: str) -> bool:
    """checking to see if string contains character"""
    i: int = 0
    assert len(single_char) == 1
    while i < len(string_one):
        if string_one[i] == single_char:
            return True
        i = i + 1
    return False

def emojified(guess_word: str, secret_word: str) -> str:
    """Testing to see if characters of guess_word are in secret_word"""
    assert len(guess_word) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001f7E8"
    empty_string: str = ""
    j: int = 0
    while j < len(secret_word):
        if guess_word[j] == secret_word[j]:
            empty_string = empty_string + GREEN_BOX
        else:
            if contains_char(secret_word, guess_word[j]):
                empty_string = empty_string + YELLOW_BOX
            else:
                empty_string = empty_string + WHITE_BOX
        j = j + 1
    return empty_string

def input_guess(expected_length: int) -> str:
    word: str = input(f"Enter a {expected_length} character word: ")
    while len(word) != expected_length:
        word = input(f"That wasn't {expected_length} chars! Try again: ")
    return word

def main() -> None:
    secret_word: str = "codes"
    num_of_guesses: int = 1
    track: bool = False
    while num_of_guesses < 7 and track is False:
        print(f"=== Turn {num_of_guesses}/6 ===")
        guess_word: str = input_guess(5)
        print(guess_word)
        print(emojified(guess_word, secret_word))
        if guess_word == secret_word:
            track = True
            print(f"You won in {num_of_guesses}/6 turns!")
        num_of_guesses = num_of_guesses + 1
        if num_of_guesses > 6 and guess_word != secret_word:
            print ("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
        
        