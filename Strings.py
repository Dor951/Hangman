import re

word = input("Please enter a string:", )
# first_let = word[0]
# print(first_let)
# rep_word = word[1:].replace(first_let, "e")
# print(first_let + rep_word)

# word_len = len(word)
# first_len = word_len//2
# second_len = word_len-first_len
# print(first_len)
# print(second_len)
# second_half = word[second_len-1:].upper()
# print(word[:second_len-1] + second_half)
print(len(word))
if len(word) > 1:
    if word.isalpha():
        print("E1 more than 1")
    elif not word.isalpha():
        print("E3 more than 1 and not english")
elif len(word) == 1 and not word.isalpha():
    print("E2 1 char not english")
else:
    print("letter is:", word.lower())

# if word.isalpha():
#     print("yes")
# else:
#     print("No")
# if re.match('[^a-zA-Z]', word):
#     print("yes")
# else:
#     print("no")
# print(re.sub('[^a-zA-Z]+', '', word))
