'''
print all the even numbers in the given range of numbers
'''

start = int(input("Beginning range: "))
end = int(input("Ending range: "))
for number in range(start, end+1):
    if number % 2 == 0:
        print(number)
