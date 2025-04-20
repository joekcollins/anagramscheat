import os
import sys
import itertools
import time

# check to make sure startup syntax is correct
if len(sys.argv) < 2:
    print("""
        The correct syntax is as follows:
        python anagramscheat.py [textfile.txt]
        This program is designed to work with wordbanks
        that have all English words between 3 and 8 characters long
         """
    )
    sys.exit(1)

text_file = sys.argv[1]
# check to make sure the wordbank txt file exists
if not os.path.exists(text_file):
    print(f"Error: the file '{text_file}' does not exist.")
    sys.exit(1)


# Code that opens the wordbank file and saves everything to a file object as a set
with open(text_file, encoding="utf-8") as f:
    wordbank = set(word.strip() for word in f)
    
# function to take user input and save the 8 characters to a list
# includes check to remove accidental white space and throw
# error code if user inputs something other than a letter
def input_characters():
    while True:
        user_input = input("Enter 6 letters: ").strip()
        if len(user_input) == 6 and user_input.isalpha():
            return list(user_input.lower())
        print("Error: that wasn't 6 characters")

# this function will take the list generated from the user input 
# and create every possible outcome of letter combinations, check to see
# if the combo is in the word bank, and if it is, add it to the possible_combo set
def word_calculator(user_input_characters, wordbank):
    possible_combos = set()
    for r in range(3, 7):
        for combo in itertools.permutations(user_input_characters, r):
            word = "".join(combo)
            if word in wordbank:
                possible_combos.add(word)    
    return (possible_combos)


# logic flow: program prompts user input -> program generates possible word combos ->
# check to see if word combos are in wordbank -> print words from wordbank -> ask the player 
# if they want to play again -> exit program
while True:
    char = input_characters()
    start = time.time()
    answers = word_calculator(char, wordbank)
    end = time.time()
    for answer in sorted(answers, key=len, reverse=True):
        print(answer)
    print(f"Found {len(answers)} words in {end - start:.2f} seconds.")
    replay = input("\nDo you want to play again? (yes/no)").strip().lower()
    if replay not in ("yes", "y"):
        print("Exiting program")
        break