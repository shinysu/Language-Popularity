'''
Using readline() to read the a single line from the file. It reads the contents of the file one line at a time.
while loop is used to read all lines from the file
'''
with open("input.txt") as reader:
    line = reader.readline()
    while line != '':
        print(line.strip('\n'))
        line = reader.readline()