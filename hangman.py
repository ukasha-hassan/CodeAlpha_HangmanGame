import random

words = ["python", "programming", "hangman", "computer", "keyboard"]
secret_word = random.choice(words)
guesses = ""
turns = 6

while turns > 0:
    failed = 0
    for char in secret_word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    if failed == 0:
        print("\nYou won! The word was", secret_word)
        break
    guess = input("\nGuess a letter: ").lower()
    guesses += guess
    if guess not in secret_word:
        turns -= 1
        print("Wrong! Turns left:", turns)
        if turns == 0:
            print("You lost! The word was", secret_word)