# assignment: programming assignment 1
# author: Peter Wang Zhao
# date: March 29, 2022
# file: hangman.py is a program that allows you to play Hangman
# input: (write input description)
# output: (write output description)

from random import choice, random
import random
dictionary_file = "dictionary.txt"   # make a dictionary.txt in the same folder where hangman.py is located

# write all your functions here

# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12

def import_dictionary (filename) :
    min_size = 2
    max_size = 12
    dictionary = {}
    try :
        file = open(filename, 'r')
        for line in file:
            line = line.strip()
            wordsize = len(line)
            if wordsize > max_size:
                wordsize = max_size
            elif wordsize < min_size:
                continue
            if wordsize in dictionary.keys():
                dictionary.get(wordsize).append(line)
            else:
                dictionary[wordsize] = []
                dictionary.get(wordsize).append(line)

    except Exception :
        print("Error.")
    return dictionary

# print the dictionary (use only for debugging)
def print_dictionary (dictionary) :
    max_size = 12
    pass 

# get options size and lives from the user, use try-except statements for wrong input
def get_game_options () :
    try:
        size = int(input("Please choose a size of a word to be guessed [3 - 12, default any size]: "))
        if size not in range (3, 13):
            print("A dictionary word of any size will be chosen.")
    except ValueError:
        size = random.randint(3, 12)
        print("The word size is set to " + str(size) + ".")
    try:
        lives = int(input("Please choose a number of lives [1 - 10, default 5]: "))
        if lives not in range (1, 11):
            raise ValueError("Out of range.")
        print("You have " + str(lives) + " lives.")
    except ValueError:
        lives = 5
        print("You have 5 lives.")
    return size, lives


# MAIN

if __name__ == '__main__' :

    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)
    print(dictionary)

    # print the dictionary (use only for debugging)
    print_dictionary(dictionary)    # remove after debugging the dictionary function import_dictionary

    # print a game introduction

    # START MAIN LOOP (OUTER PROGRAM LOOP)
    while True:
        print("Welcome to the Hangman Game!")

    # set up game options (the word size and number of lives)
        gameoptions = get_game_options()
    # select a word from a dictionary (according to the game options)
        print(dictionary.get(gameoptions[0]))
        word = choice(dictionary.get(gameoptions[0]))
        print(word)

        # START GAME LOOP   (INNER PROGRAM LOOP)
        while True:
        # format and print the game interface:
            print("Letters chosen:")
            print("__ __ __ __ __ lives: " + str(gameoptions[1]) + " OOOOO")
            print("Please choose a new letter > ")
        # Letters chosen: E, S, P                list of chosen letters

        # __ P P __ E    lives: 4   XOOOO        hidden word and lives

        # ask the user to guess a letter

        # update the list of chosen letters

        # if the letter is correct update the hidden word,
        # else update the number of lives
        # and print interactive messages      

        # END GAME LOOP   (INNER PROGRAM LOOP)
            break
        # check if the user guesses the word correctly or lost all lives,
        # if yes finish the game

    # END MAIN LOOP (OUTER PROGRAM LOOP)

    # ask if the user wants to continue playing,


        answer = input("Would you like to play again [Y/N]? ")
        if answer == "Y" or answer == "y":
            get_game_options()
        else:
            print("Goodbye!")
            break
    # if yes start a new game, otherwise terminate the program
