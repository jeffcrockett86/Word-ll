import sys
import random

"""
>>> play('a') & play('p') & play('l') & play('e')
{'plane', 'pearl', 'leapt', 'place', 'penal', 'maple', 'lapse', 'plate',
'ample', 'paler', 'pedal', 'apple', 'pleat', 'panel', 'plead', 'petal', 'lapel'}
"""

"""
from game import *
oag=orange_and_green
oag('white')
"""

f = open('wordleAlpha.txt', 'r')
sys.argv = ['slant', 'guest', 'reach', 'whirl']
words = [word for word in f.read().split('\n')][:-1]
answer = 'hello'

def words_with(letter, words=words):
    return [word for word in words if letter in word and letter in answer]


def orange_and_green(word):
    output = []
    for i in range(len(word) - 1):
        set1 = set(words_with(word[i]))
        set2 = set(words_with(word[i+1]))
        output.append((set1, set2))
        print(output[-1])
        # output = list(set(output[-1][0] & output[-1][1]))
        output.append(word[i])
        # print('output[index] is', output[i])

    return output


# def play(word, guess_num, words=words):
#     guess_num += 1
#     print('word is', word)
#     print('guess num is', guess_num)
#     # answer = 'hello'
#     # print(answer)
#     if guess_num > 4 or len(word) == 0:
#         return {}
#     sys.argv = sys.argv[1:]
#     print(sys.argv)
#     print('word is', word)
#     return set(word[0]) & set(list(play(word[1:], guess_num, words_with(word[0]))))
#     # return set([play(letter, num_guesses=num_guesses) for letter, i in word[] if letter in word and letter in answer])


# print('words with slant', play('holho', 0))
