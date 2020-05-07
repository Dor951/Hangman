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


def is_valid_input(letter_guessed):
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
        return True


MAX_TRIES = 6
print(HANGMAN_ASCII_ART)
print("Total number of tries:", MAX_TRIES)
select_word = input("Please enter a word:", )
print_space(select_word)
letter = input("Guess a letter:", )
print(is_valid_input(letter))

print(random.randint(5, 10))

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
