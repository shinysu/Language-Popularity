'''
A contactbook app where you store the contact names and phone numbers using dictionary
Edit the phone number of a contact
if the name is not found, then it will add a new contact with that name
'''

def edit_contact():
    name = input("Enter the name of the contact to be edited: ")
    new_number = int(input("Enter the new phone number"))
    contactbook[name] = new_number


contactbook = {'Arun': 999999, 'Ben':888888}
edit_contact()
print(contactbook)