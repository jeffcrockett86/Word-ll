import random
import termcolor
import re

#open the file
f = open('wordleAlpha.txt')
words = f.read().split('\n')
#turn the file's text into a string


# print(text)

#generate 5 letter words from the text file

row = ['_', '_', '_', '_', '_']
# print(words)
#answer is random word from words
answer = words[random.randint(0, len(words) - 1)]

def display_instructions():
    print(termcolor. colored('---', 'red') + ' means wrong letter wrong place\n')
    print(termcolor. colored('---', 'white') + ' means wrong letter wrong place\n')
    print(termcolor. colored('---', 'yellow') + ' means right letter wrong place\n')

def valid(guess):
   if re.match(r'^[A-Za-z]{5}$', guess):
     return True
   else:
     return False
#make sure guess's length is 5 and it only has letters
# def validate_and_check(guess):
#     if re.match(f'^[a-zA-Z]{5}$', guess):
#         for letter in word:
#             check(letter)
#     else:
#        print('asdf')

# validate = guess: re.match(r'^[A-Za-z]{5}$', guess)

#check returns the letter but with the right color
def check(guess, guess_count=0):
    if guess == answer:
        print(termcolor.colored(answer, 'green'))
        print("You win!")
        return
    if not valid(guess):
        print('Invalid guess')
        guess = input(' '.join(row))
        check(guess)
    while guess_count < 6:
        guess_count +=1
        print('answer is', answer)
        print('guess count is', guess_count)
        for i in range(len(guess)):
            # print(guess[i])
            #if right letter right place
            if guess[i] == answer[i]:
                row[i] = termcolor.colored(guess[i], 'green')

        #if right letter wrong place
            elif guess[i] in answer and guess[i] != answer[i]:
                row[i] = termcolor.colored(guess[i], 'yellow')
            else:
                continue

        guess = input(''.join(row) + '\n\n')
        # print('guess is', guess)
        # guess_count += 1
        print('guess count is', guess_count)
        guess = str(guess[:5])
        # if guess == answer:
        #     print(termcolor.colored(guess, 'green'))
        #     print("You win!")
        #     return
        check(guess, guess_count)

    # if right_letter_wrong_place(letter):
    #     return input([termcolor.colored(letter, 'yellow')] + [check(each_letter) for each_letter in guess])#]]termcolor. colored('---', 'red') + ' means wrong letter wrong place') +
    # if right_letter_right_place(letter):
    #     return input(termcolor.colored(letter, 'yellow'))
    # else:
    #     return input(termcolor.colored(letter, 'white'))

#display the instructions
def display_instructions():
    print(termcolor. colored('---', 'red') + ' means wrong letter wrong place')
    print(termcolor. colored('---', 'white') + ' means wrong letter wrong place')
    print(termcolor. colored('---', 'yellow') + ' means right letter wrong place')
inp = input("Welcome to Word'll! Press x to see instructions. Press any other key to begin.\n\n")
if inp.lower() == 'x':
    display_instructions()

else:
    guess = input(' '.join(row) + '\n\n')
    # while(guess != answer):

    # if valid(guess):
    check(guess)

# answer = 'apple'
# guess = 'azzzz'
# print(guess)
# while(guess != answer):
#     validate(guess)
#     break
# print('You win!')
# check([letter for letter in guess]]
