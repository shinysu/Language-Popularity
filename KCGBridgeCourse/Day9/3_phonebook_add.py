'''
A contactbook app where you store the contact names and phone numbers using dictionary
Add a new contact into the contactbook
'''

def add_contacts():
    name = input("Enter the name: ")
    number = int(input("Enter the phone number"))
    contactbook[name] = number


contactbook = {'Arun': 999999, 'Ben':888888}
add_contacts()
print(contactbook)