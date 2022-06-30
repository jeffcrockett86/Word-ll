import sys
import random

f = open('wordleAlpha.txt', 'r')
sys.argv = ['slant', 'guest', 'reach', 'whirl']
words = [word for word in f.read().split('\n')][:-1]
answer = 'hello'


def words_with(letter):
    return set([word for word in words if letter in word])


def play_game_beta(the_words=words, guess=sys.argv[0], guess_num=0, words_left=[]):
    print('answer is', answer)
    print('guess is', guess)
    guess_num += 1
    if guess == answer:
        return 'You win!'

    #base case
    if guess_num >= 6 or len(sys.argv) == 0:
        return {}

    if 0 < guess_num <= 4:
        words_left.append(words_with(guess[guess_num]))
        """& play_game_beta(the_words=words_with(guess[guess
        _num]), guess=sys.argv[0], guess_num=guess_num, words_left=words_left))
        """
        print('words left:', words_left)
    return words_left


print(play_game_beta())
