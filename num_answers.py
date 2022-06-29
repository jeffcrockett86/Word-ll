import sys
import re

f = open('wordleAlpha.txt', 'r')
words = [word for word in f.read().split('\n')][:-1]
print(words)

a = 97
z = 123
alphabet = [chr(i) for i in range(a, z)]
print(alphabet)

string = ''.join(words)
tuples = sorted([(letter, len(re.findall(f"{letter}", string)) / 2315) for letter in alphabet], key=lambda x: x[1])

print(tuples)

# print(sys.argv)
