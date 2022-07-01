import sys
import random

# >>> set(word_matches('h')) & set(word_matches('e'))& set(word_matches('l')) & set(word_matches('o'))
# {'hello', 'hovel', 'hotel', 'whole'}


f = open('wordleAlpha.txt', 'r')
sys.argv = ['slant', 'guest', 'reach', 'whirl']
words = [word for word in f.read().split('\n')][:-1]
answer = 'hello'


# def yellow(letter, words=words):
#     return [(word, i) for i in range(len(words)) if word[i] in answer and word[i] != answer[i]]

def green(letter, words):
    output = []
    for word in words:
        for i in range(len(word)):
            output.append([[word, i] for i in range(len(word)) if word[i] in answer and word[i] == answer[i]])
    # return [(word, i) for i in range(len(words)) if word[i] in answer and word[i] != answer[i]]
    return output

def yellow(letter, words):
    output = []
    for word in words:
        for i in range(len(word)):
            output.append([[word, i] for i in range(len(word)) if word[i] in answer and word[i] != answer[i]])
    # return [(word, i) for i in range(len(words)) if word[i] in answer and word[i] != answer[i]]
    return output

g = green('h', words)
pairs = [x for x in g if len(x) > 0]
new_words = [pair[0] for pair in pairs]
print(len(new_words[0]))
# new_words_beta =
# def orange_and_green(word, words=words):
#     output = []
#     for i in range(len(word) - 1):
#         set1 = set(word_matches(word[i]))
#         set2 = set(word_matches(word[i+1]))
#         output.append((set1, set2))
#         output.append(word[i])
#     return output


# test = [orange_and_green(word)[0][0] for word in sys.argv]
