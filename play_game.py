import sys
import random

f = open('wordleAlpha.txt', 'r')
sys.argv = ['slant', 'guest', 'reach', 'whirl']
words = [word for word in f.read().split('\n')][:-1]
# answer = words[random.randint(0, len(words) - 1)]
answer = 'hello'

def words_with(letter):
    return set([word for word in words if letter in word])


# def letter_in_guess_and_answer(letter, guess, answer):
#     return letter in guess and letter in answer

def play_game_beta(the_words=words, guess=sys.argv[0], guess_num=0, words_left=[]):
    print('answer is', answer)
    print('guess is', guess)
    guess_num += 1
    if guess == answer:
        return 'You win!'

    #base case
    if guess_num >= 6 or len(sys.argv) == 0:
        # print('words left', words_left)
        return {}
    if 0 < guess_num <= 4:
        words_left.append((words_with(guess[guess_num])) & play_game_beta(the_words=words_with(guess[guess_num]), guess=sys.argv[0], guess_num=guess_num, words_left=words_left))
        print('words left:', words_left)
    return words_left


# def run_guesses(guess):
#     print(guess)

#     bool_tuples = [(letter,letter_in_guess_and_answer(letter, guess, answer)) for letter in guess]
#     letters_in_common = [tup[0] for tup in bool_tuples if tup[1]]
#     d = {letter: list(set(words_with(letter))) for letter in letters_in_common}
#     set_d = set([letters_with(val) for val in d]) & run_guesses
#     return set_d


# def play_game(word_list, num_guesses=0, guess=sys.argv[1]):
#     letters = run_guesses(guess)
#     print('letters is', letters)
#     try:
#         word_set = set(list(letters.values()))
#     except KeyError:
#         word_set = set(word_list)
#     num_guesses += 1
#     while num_guesses < 2 or len(sys.argv) != 0:
#         print(f'Guess {num_guesses}')
#         # for key in letters:
#         play_game(list(word_set), num_guesses=num_guesses, guess=sys.argv[1:][1] )
#     return word_set

# print(play_game(words))


    # for i in range(len(guess)):
    #     # if i == 0:
    #     #     available_words = set(words_with(guess[i])) & set(words_with(guess[i+1]))
    #     # words_left.append(set(words_with(guess[i])))
    #     # words_left.append(set((guess[i])) & play_game_beta(the_words=words_with(guess[i]), guess=sys.argv[0], guess_num=guess_num, words_left=words_left))
    #     print('words left', words_left)
    #     # print('words left', words_left)
    #     sys.argv = sys.argv[1:] if len(sys.argv) > 1 else sys.argv
    #     # print('sys.argv is', sys.argv[i])
    #     # print(f'words with {guess[i]}',words_with(guess[i]) if guess)
    #     return set((words_with(guess[i]))) & play_game_beta(the_words=words_with(guess[i]), guess=sys.argv[0], guess_num=guess_num, words_left=words_left)

        # if i == len(guess)-1:
        #     return words_with(guess[i])
    # print('available words: ', available_words)
    # return play_game_beta(words=available_words, guess=sys.argv[1:][1], guess_num=guess_num)

# print('answer is', answer)
# print(play_game_beta())
print([list(s) for s in play_game_beta()])
# print(play_game_beta()[1])

# print(play_game_beta()[2])
