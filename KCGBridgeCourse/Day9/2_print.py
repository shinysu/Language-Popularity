'''
Prints all the names, birthdays from the birthday calendar
concepts - how to get the keys, values from a dictionary
'''
birthdays = {'Arun': '01-09-2002', 'Ben':'08-12-2001', 'Cathy':'21-04-2001'}

names = birthdays.keys()
dates = birthdays.values()
print(list(names))
print(list(dates))
for key, value in birthdays.items():
    print(key, value)