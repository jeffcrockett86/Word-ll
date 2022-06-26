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

def validate(guess):
   if re.match(r'^[A-Za-z]{5}$', guess):
     print ('match')
   else:
     print ('no match')
#make sure guess's length is 5 and it only has letters
# def validate_and_check(guess):
#     if re.match(f'^[a-zA-Z]{5}$', guess):
#         for letter in word:
#             check(letter)
#     else:
#        print('asdf')

# validate = guess: re.match(r'^[A-Za-z]{5}$', guess)

#check returns the letter but with the right color
def check(letter):
    if right_letter_wrong_place(letter):
        return input([termcolor.colored(letter, 'yellow')] + [check(each_letter) for each_letter in guess])#]]termcolor. colored('---', 'red') + ' means wrong letter wrong place') +
    if right_letter_right_place(letter):
        return input(termcolor.colored(letter, 'yellow'))
    else:
        return input(termcolor.colored(letter, 'white'))

print(termcolor. colored('---', 'red') + ' means wrong letter wrong place')
print(termcolor. colored('---', 'white') + ' means wrong letter wrong place')
print(termcolor. colored('---', 'yellow') + ' means right letter wrong place')

guess = 'azzzz'
print(guess)
# while(guess != answer):
#     validate_and_check(guess)
# print('You win!')
# check([letter for letter in guess]]
