# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 16:53:08 2025

@author: kimbe
"""

import random

def draw_hangman(lives):
    stages = [
        """
         ----
         |  |
         |  O
         | /|\\
         | / \\
         |
       --------
        """,
        """
         ----
         |  |
         |  O
         | /|\\
         | / 
         |
       --------
        """,
        """
         ----
         |  |
         |  O
         | /|\\
         |
         |
       --------
        """,
        """
         ----
         |  |
         |  O
         | /|
         |
         |
       --------
        """,
        """
         ----
         |  |
         |  O
         |  |
         |
         |
       --------
        """,
        """
         ----
         |  |
         |  O
         |
         |
         |
       --------
        """,
        """
         ----
         |  |
         |
         |
         |
         |
       --------
        """
    ]
    print(stages[lives])


def easy():
    #Returns a random 3-letter word.
    words = ["the", "had", "nap", "ham", "can", "cat", "tap"]
    return random.choice(words)


def medium():
    #Returns a random 5-letter word.
    words = ["eager", "label", "imply", "cacti", "easer", "caddy", "sheep"]
    return random.choice(words)


def hard():
    #Returns a random 7-letter word.
    words = ["because", "hangman", "pretzel", "puzzled", "monster", "blanket"]
    return random.choice(words)


def main():
    print("Welcome to the Hangman Game!")
    print("There are 3 gamemodes:")
    print("- Easy: 3-letter word")
    print("- Medium: 5-letter word")
    print("- Hard: 7-letter word")
    
    while True:
        try:
            game_mode = int(input("\nChoose a mode: Easy (3), Medium (5), or Hard (7): "))
            if game_mode == 3:
                word = easy()
            elif game_mode == 5:
                word = medium()
            elif game_mode == 7:
                word = hard()
            else:
                print("Invalid choice. Please choose 3, 5, or 7.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    guesses = 6
    guessed_letters = ""

    while guesses > 0:
        print("\nWord:", end=" ")
        display_word = "".join([char if char in guessed_letters else "_" for char in word])
        print(" ".join(display_word))

        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word correctly!")
            break

        letter = input("\nGuess a letter: ").lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single valid letter.")
            continue

        if letter in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters += letter

        if letter not in word:
            guesses -= 1
            print(f"❌ Incorrect guess! You have {guesses} lives left.")
            draw_hangman(guesses)
        else:
            print("✅ Correct guess!")

    if guesses == 0:
        print("\n💀 You lost! The word was:", word)

    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        main()
    else:
        print("\nThanks for playing Hangman! 👋")


if __name__ == "__main__":
    main()
