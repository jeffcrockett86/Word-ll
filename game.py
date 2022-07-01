import sys
import random


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
        output.append(word[i])
    return output

print([list(orange_and_green('hxxxx'))[0][i] for i in range(2)][0] == set(words_with('h')))
