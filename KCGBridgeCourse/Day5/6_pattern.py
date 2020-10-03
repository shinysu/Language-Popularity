"""
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
"""

def plus_line():
    print("+ ", end='')
    for i in range(4):
        print('- ', end='')
    print("+ ",end='')
    for i in range(4):
        print('- ', end='')
    print("+")

def other_line():
    print("| ", end='')
    for i in range(4):
        print("  ", end='')
    print("| ", end='')
    for i in range(4):
        print("  ", end='')
    print("|")


for x in range(1, 12):
    if x == 1 or x == 6 or x == 11:
        plus_line()
    else:
        other_line()