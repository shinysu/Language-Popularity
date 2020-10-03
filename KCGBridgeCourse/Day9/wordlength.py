'''
A program to store the length of the words of a string in a dictionary
key will be the word and value will be the length of the word
'''

line = 'A quick brown fox jumped over the lazy dog'
words = line.split()
wordlength = {}
for x in words:
    wordlength[x] = len(x)

print(wordlength)

