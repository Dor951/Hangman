#last update 18.05

import random
import re

HANGMAN_ASCII_ART = ("""
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/""")

HANGMAN_PHOTOS = {
    1: """    x-------x""", 
    2: """
    x-------x
    |
    |
    |
    |
    |""", 
    3: """
    x-------x
    |       |
    |       0
    |
    |
    |
    """,
    4: """
    x-------x
    |       |
    |       0
    |       |
    |
    |""", 
    5: """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""",
    6: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
    """,
    7: """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """ }

def print_space(word):
    return("_ " * len(word))

def check_valid_input(letter_guessed, old_letters_guessed):
    if len(letter_guessed) > 1:
        if letter_guessed.isalpha():
            print("E1 more than 1")
            return False
        elif not letter_guessed.isalpha():
            print("E3 more than 1 and not english")
            return False
    elif len(letter_guessed) == 1 and not letter_guessed.isalpha():
        print("E2 1 char not english")
        return False
    else:
        # print("letter is:", letter_guessed.lower())
        if letter_guessed.lower() not in (old_letters_guessed):
            return True
        else:
            return False

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if(check_valid_input(letter_guessed, old_letters_guessed)):
        old_letters_guessed.append(letter_guessed)
        return True
    else: 
        print("X")
        s = " -> "
        old_letters_guessed.sort()
        [x.lower() for x in old_letters_guessed]
        old_letters_guessed = s.join(old_letters_guessed)
        print(old_letters_guessed)
        return False

# to go over the all list of old letters
def show_hidden_word(secret_word, old_letters_guessed):
    hidden = print_space(secret_word)
    list_from_string = list(hidden)
    # last_letter = old_letters_guessed[-1]
    for letter in old_letters_guessed:
        for i, char in enumerate(secret_word):
                if char == letter:
                    if i == 0:
                        list_from_string[i] = char
                    else:
                        list_from_string[i+i] = char

    hidden = ''.join(list_from_string)
    return hidden

def check_win(secret_word, old_letters_guessed):
    correct_Letters = [None] * len(secret_word)
    for letter in old_letters_guessed:
        if letter in secret_word:
            # print("search for the letter: ", letter)
            # print("location in the list is: ",secret_word.find(letter))
            correct_Letters[secret_word.find(letter)] = secret_word[secret_word.find(letter)]
            # print("correct Letters list in loop is: ",correct_Letters)
        
    correct_Letters = [str(i or '_') for i in correct_Letters] 
    correct_Letters = ''.join(correct_Letters)
    if correct_Letters == secret_word:
        print("WIN")
        return True
    else:
        # print("Not equal")
        # print("correct Letters list in results is: ",correct_Letters)
        # print("secret word  is: ",secret_word)
        return False

def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])

def choose_word(file_path, index):
    input_file = open(file_path, "r")
    file_data = input_file.read().split(" ")
    file_data_no_dupl = set(file_data)
    file_len = len(file_data)
    file_len_no_dupl = len(file_data_no_dupl)
    if index > file_len:
        while index  > file_len:
            index = index - file_len
        return(file_data[index-1])
    else:
        return(file_data[index-1])

def main():
    MAX_TRIES = 7
    old_letters = []
    num_of_tries = 1
    print(HANGMAN_ASCII_ART)

    # file_path = input("Please enter the file path: ")
    word_num = int(input("Please enter an index: "))
    selected_word = (choose_word(r"words.txt", word_num))
    print("Total number of tries:", MAX_TRIES-1)
    print(HANGMAN_PHOTOS[num_of_tries])
    
    while check_win(selected_word, old_letters) == False:
        letter = input("Guess a letter: ", ).lower()
        # print(check_valid_input(letter, old_letters))
        if try_update_letter_guessed(letter, old_letters) == True:
            print(show_hidden_word(selected_word, old_letters))
        else:
            print("number of tries: ", num_of_tries)
            num_of_tries += 1
            print(HANGMAN_PHOTOS[num_of_tries])
            if num_of_tries == MAX_TRIES:
                print("You Lose")
                break

    # print(random.randint(5, 10))

if __name__ == "__main__":
    main()