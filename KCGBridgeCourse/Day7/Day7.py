'''
check if an element is present in the list
you can use 'in' operator to check if the element is present and 'not in' operator to check if the element is not present
'''

cart = ['ice cream', 'chocolates', 'bread', 'jam', 'butter']
item = input("Enter the element you want to search: ")

if item in cart:
    print("yes, the element is present")
else:
    print("No, the element is not present")
