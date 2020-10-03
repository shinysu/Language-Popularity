'''
Count the occurance of each letter in the given string.
Eg:- s occurs 8 times, h - 4 times etc
'''

line = 'she sells sea shells in the sea shore'
lettercount = {}
for x in line:
    if x in lettercount:
        lettercount[x] = lettercount[x] + 1
    else:
        lettercount[x] = 1

print(lettercount)