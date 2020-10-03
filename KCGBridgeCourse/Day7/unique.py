'''
remove duplicate elements from a given list
sample input : [1, 2, 1, 3, 2]
sample output: [1, 2, 3]
'''
def remove_duplicates(original):
    unique = []
    for x in original:
        if x not in unique:
            unique.append(x)
    return unique

numbers = []
n = int(input("Enter the number of elements:"))
for i in range(n):
    num = int(input())
    numbers.append(num)

unique = remove_duplicates(numbers)
print(unique)
