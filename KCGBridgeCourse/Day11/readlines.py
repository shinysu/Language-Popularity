'''
Using readlines() to read the contents of the file. It reads the contents of the file and returns a list of lines.
strip('\n') is used to strip the newline character from the end of the string
'''
with open("input.txt") as reader:
    lines = reader.readlines()
    for x in lines:
        print(x.strip('\n'))