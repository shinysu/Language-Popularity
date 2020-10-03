'''
program to read from a file using read() and write to another file using write()
'''
with open("input.txt","r") as reader:
    lines = reader.read()

with open("output.txt","w") as writer:
    writer.write(lines)