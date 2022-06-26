import random
import termcolor
import re

#open the file
f = open('computer.txt', 'r')

#turn the file's text into a string
text = f.read()

print(text)

#generate 5 letter words from the text file
words = [word.lower() for word in text.split() if len(word) == 5]

#answer is random word from words
answer = words[random.randint(0, len(words))]

#make sure guess's length is 5 and it only has letters
def validate_and_check(word):
    if re.match(f'^[a-zA-Z]{5}$', word):
        for letter in word:
            check(letter)


def check(letter):
    if right_letter_wrong_place(letter):
        next_guess = input(termcolor.colored(letter, 'yellow'))

    if right_letter_right_place(letter):
        next_guess = input(termcolor.colored(letter, 'yellow'))
    else:
        next_guess = input(termcolor.colored(letter, 'white'))

print(termcolor. colored('---', 'red') + ' means wrong letter wrong place')
print(termcolor. colored('---', 'white') + ' means wrong letter wrong place')
print(termcolor. colored('---', 'yellow') + ' means right letter wrong place')

guess = input('_ _ _ _ _\n\n')
while(guess != answer):
    validate_and_check(guess)
print('You win!')
# check([letter for letter in guess]]
