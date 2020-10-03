'''
find the minimum value in the given list
'''

def find_minimum(numbers):
    minimum = numbers[0]
    for x in numbers:
        if x < minimum:
            minimum = x
    return minimum

numbers = []
n = int(input("Enter the number of elements:"))
for i in range(n):
    num = int(input())
    numbers.append(num)

minimum = find_minimum(numbers)
print(minimum)
