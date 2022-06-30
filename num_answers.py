import sys
import re
import random

f = open('wordleAlpha.txt', 'r')
words = [word for word in f.read().split('\n')][:-1]
# def gen_dict():

#     # print(words)

#     a = 97
#     z = 123
#     alphabet = [chr(i) for i in range(a, z)]
#     #print(alphabet)

#     # string = ''.join(words)
#     # tuples = sorted([(letter, len(re.findall(f"{letter}", string)) / 2315) for letter in alphabet], key=lambda x: x[1])

#     # print(tuples)

#     list1 = [pair[0] for pair in tuples]
#     list2 = [pair[1] for pair in tuples]

#     sorted_vowels = dict(zip(list1, list2))
#     # print(sorted_vowels)
#     percentages = ["{0:.0%}".format(item) for item in list2]
#     new_sorted_vowels = dict(zip(list1, percentages))
#     return new_sorted_vowels


# def look_up_percentage(letter):
#     return gen_dict()[letter]

def gen_tuples(letter):
    return [(word,len(re.findall(re.compile(letter), word))) for word in words]

# gen_dict()
# print(look_up_percentage('j'))

# def gen_tuples2(letter):
#     fil = filter(gen_tuples, lambda x: x[1] == 1)
#     print('filter:', fil)

def words_with(letter):
    return [word[0] for word in gen_tuples(letter) if word[1] == 1]

# print(words_with('k'))
# guesses = sys.argv
# print(guesses)
# guesses = guesses[1:]
# print(guesses)
# words = words_with('k')
# print(words)
# words = words_with('s')
# print(words)

def letter_in_guess_and_answer(letter, guess, answer):
    return letter in guess and letter in answer


def filter_list(ls, guess, answer):
    return set(filter((lambda x: x in guess and x in answer), ls))


def run_guesses(guesses):
    f = open('wordleAlpha.txt', 'r')
    words = [word for word in f.read().split('\n')][:-1]
    word_list = []
    tries = 0
    print(guesses)
    answer = words[random.randint(0, len(words) - 1)]
    # print(type(words[random.randint(0, len(words) - 1)]))
    print('answer is', answer)
    # while(tries <= 5):
    #     tries += 1
    print(f'Guess {tries}')

    for guess in guesses:
        # print('guess is', guess)

        bool_tuples = [(letter,letter_in_guess_and_answer(letter, guess, answer)) for letter in guess]
        print('bool_tuples is', bool_tuples)
        # print('bool_tuples is', bool_tuples)
        words = [item[0] for item in bool_tuples if item[1]]
        print('words is', words)
        # print(words)

            # words = list(filter(letter_in_word, words))
            # print('words is', words)
            # word_list.append(words)
            # print(word_list)
        if len(words) > 0:
                continue
        if len(words) == 1:
                print("You win!")
                return bool_tuples

    letters_in_common = [tup[0] for tup in bool_tuples if tup[1]]
    d = {letter: words_with(letter) for letter in letters_in_common}
    # return letters_in_common
    return d

letters = run_guesses(sys.argv[1:])
# print(letters)
print("There are", len(set([word for ls in letters.values() for word in ls])), 'words left', set([word for ls in letters.values() for word in ls]) )
# available_words = set([letters.values()])
# print(available_words)
# print(letters.items())
# print('words with e:', words_with('est'))
# print([words_with(letter) for letter in letters])

# print([pair[0] for pair in run_guesses(sys.argv[1]) ])
