import sys
import re


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

def run_guesses(guesses):
    f = open('wordleAlpha.txt', 'r')
    words = [word for word in f.read().split('\n')][:-1]

    tries = 1
    print(guesses)
    while(tries <= 6):
        print(f'Guess {tries}')
        tries += 1
        for guess in guesses:
            for letter in guess:

                #narrow down list of words

                words = list(filter(lambda word: letter in word, words))
                if len(words) > 0:
                    print(words)
    return words

run_guesses(sys.argv[1:])
