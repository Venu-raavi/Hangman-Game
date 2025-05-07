# hangman.py

import random
from words import word_categories

def choose_random_category():
    return random.choice(list(word_categories.keys()))

def choose_word(category):
    return random.choice(word_categories[category]).lower()

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter == ' ':
            display += '  '  # show space automatically
        elif letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def hangman():
    print("Welcome to Hangman!")
    category = choose_random_category()
    word_to_guess = choose_word(category)
    guessed_letters = set()
    attempts_left = 6

    print(f"\nThe category is: {category.replace('_', ' ').capitalize()}")
    print(f"The word has {len(word_to_guess.replace(' ', ''))} letters (excluding spaces).")

    while attempts_left > 0:
        print("\n" + display_word(word_to_guess, guessed_letters))
        print(f"Attempts remaining: {attempts_left}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts_left -= 1

        if all(letter in guessed_letters or letter == ' ' for letter in word_to_guess):
            print("\n🎉 Congratulations! You guessed the word:", word_to_guess.upper())
            break
    else:
        print("\n💀 Game over! The word was:", word_to_guess.upper())

if __name__ == "__main__":
    hangman()
