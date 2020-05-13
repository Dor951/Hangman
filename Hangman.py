#last update 13.05

import random
import re


def print_space(word):
    print("_ " * len(word))


HANGMAN_ASCII_ART = ("""
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/""")


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
        print("letter is:", letter_guessed.lower())
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


MAX_TRIES = 6
old_letters = ['a', 'p', 'c', 'f']
print(HANGMAN_ASCII_ART)
print("Total number of tries:", MAX_TRIES)
select_word = input("Please enter a word:", )
print_space(select_word)
letter = input("Guess a letter:", )
# print(check_valid_input(letter, old_letters))
print(try_update_letter_guessed(letter, old_letters))
print("Guessed letters so far:", old_letters)
# print(random.randint(5, 10))

# print("""picture 1:
#     x-------x""")
#
# print("""picture 2:
#     x-------x
#     |
#     |
#     |
#     |
#     |""")
#
# print("""picture 3:
#     x-------x
#     |       |
#     |       0
#     |
#     |
#     |
# """)
#
# print("""picture 4:
#     x-------x
#     |       |
#     |       0
#     |       |
#     |
#     |""")
#
# print("""picture 5:
#     x-------x
#     |       |
#     |       0
#     |      /|\\
#     |
#     |""")
#
# print("""picture 6:
#     x-------x
#     |       |
#     |       0
#     |      /|\\
#     |      /
#     |
# """)
#
# print("""picture 7:
#     x-------x
#     |       |
#     |       0
#     |      /|\\
#     |      / \\
#     |
# """)
