'''
print the numbers in a given range while incrementing by 4
The range() takes a third argument, step that increments the number by that value after every iteration
'''

start = int(input("Beginning range: "))
end = int(input("Ending range: "))
for number in range(start, end+1, 4):
    print(number)