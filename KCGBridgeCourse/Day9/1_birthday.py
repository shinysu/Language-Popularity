'''
A birthday calendar using dictionary where you can search a name and get the birthday of the person
Concept : how to get a value from the dictionary by using the key
'''
birthdays = {'Arun': '01-09-2002', 'Ben':'08-12-2001', 'Cathy':'21-04-2001'}

print("Birthday calendar")
name = input("Enter the name: ")
print(birthdays[name])
