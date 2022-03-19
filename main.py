import os
import random
from utils import Utils


def clear_board():
    """Clear the board to start the game
    """
    os.system("cls")


def get_word() -> str:
    """Get a random word from data.txt

    Returns:
        str: Selected word to guess in the game.
    """
    with open("./data.txt", "r", encoding="utf-8") as f:
        words = [line.strip().lower() for line in f]

    word = random.choice(words)
    return word


def remove_accents_from_a_word(word: str) -> str:
    """Remove the acents from the word to use in the game

    Args:
        word (str): Word selected

    Returns:
        str: Word with accents removed
    """
    word_without_accent = word.maketrans("áéíóú", "aeiou")
    return word.translate(word_without_accent)


def run():

    life_counter = 7
    fail_attemps = 0

    play_word = remove_accents_from_a_word(get_word())
    secret_word = ["_"] * len(play_word)

    while True:

        clear_board()
        print(Utils.welcome_screen)
        print(Utils.HANGMANPICS[fail_attemps])
        print(f"Lives: {life_counter}")

        [print(character, end=" ") for character in secret_word]

        input_letter = input("\n\nType a letter to guess the hidden word: ")
        input_letter  = remove_accents_from_a_word(input_letter.lower())
        

        character_found = False
        for idx, character in enumerate(play_word):
            if input_letter == character:
                secret_word[idx] = input_letter
                character_found = True

        if not character_found:
            life_counter -= 1
            fail_attemps += 1

        if "_" not in secret_word:
            clear_board()
            print(Utils.welcome_screen)
            print(Utils.HANGMANPICS[-1])
            print(f"You won, the word was: {play_word}")
            break

        if fail_attemps > 6:
            clear_board()
            print(Utils.welcome_screen)
            print(Utils.HANGMANPICS[7])
            print(f"You Lost, the word was {play_word}")
            break


if __name__ == "__main__":
    run()
