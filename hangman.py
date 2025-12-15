=================================
      WELCOME TO HANGMAN         
=================================

Word to guess:  _ _ _ _ 
Lives remaining: 6
---------------------------------
Please enter a letter: p
Nice! 'p' is in the word.

Word to guess:  l o o p 
Lives remaining: 6
---------------------------------

*** CONGRATULATIONS! ***
You guessed the word: LOOP
You are a Python Master!# ---------------------------------------------------------
# Project: Hangman Game (Task 1)
# Author: Intern (B.Tech 2nd Year)
# Description: A text-based game where you guess the word.
#              Created for Python training module.
# ---------------------------------------------------------

import random

def start_game():
    # predefined list of words as per requirements
    words_database = ["python", "coding", "loop", "string", "list"]
    
    # Choosing a random word from the database
    secret_word = random.choice(words_database)
    
    # Game variables
    lives_left = 6
    guessed_letters = []  # List to store letters user has tried
    game_over = False

    # Added some ASCII art to make it look better! 
    print("=================================")
    print("      WELCOME TO HANGMAN         ")
    print("=================================")
    
    while not game_over:
        # 1. Print current status of the word
        # This loop creates the "_ _ a _" string
        display_string = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_string += letter + " "
            else:
                display_string += "_ "
        
        print(f"\nWord to guess:  {display_string}")
        print(f"Lives remaining: {lives_left}")
        print("---------------------------------")

        # 2. Check if user won
        if "_" not in display_string:
            print("\n*** CONGRATULATIONS! ***")
            print(f"You guessed the word: {secret_word.upper()}")
            print("You are a Python Master!")
            game_over = True
            break
        
        # 3. Check if user lost
        if lives_left == 0:
            print("\n:( GAME OVER :(")
            print(f"The correct word was: {secret_word}")
            print("Better luck next time!")
            game_over = True
            break

        # 4. Taking Input
        user_guess = input("Please enter a letter: ").lower()

        # VALIDATION: Checking edge cases
        if len(user_guess) != 1:
            print(">> Error: Please enter exactly one letter.")
            continue
        if not user_guess.isalpha():
            print(">> Error: Only alphabets are allowed.")
            continue
        if user_guess in guessed_letters:
            print(f">> You already guessed '{user_guess}'. Try another one.")
            continue

        # Adding guess to our list
        guessed_letters.append(user_guess)

        # 5. Logic to check if guess is correct or wrong
        if user_guess in secret_word:
            print(f"Nice! '{user_guess}' is in the word.")
        else:
            lives_left -= 1
            print(f"Oops! '{user_guess}' is NOT in the word.")

# Calling the function to run the code
start_game()