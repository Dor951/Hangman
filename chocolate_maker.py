def chocolate_maker(small, big, x):
    smallSum = small * 1
    bigSum = big * 5
    if x - bigSum - smallSum <= 0:
        return True
    else:
        return False


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


def main():
    # print(chocolate_maker(3, 1, 8))
    # print(chocolate_maker(3, 1, 9))
    # print(chocolate_maker(3, 2, 10))
    print(is_valid_input('a'))
    print(is_valid_input('A'))
    print(is_valid_input('$'))
    print(is_valid_input("ab"))
    print(is_valid_input("app$"))


if __name__ == "__main__":
    main()
