'''
A contactbook app where you store the contact names and phone numbers using dictionary
delete a contact from the contactbook
'''

def delete_contact():
    name = input("Enter the name of the contact to be removed: ")
    if name in contactbook:
        del contactbook[name]
    else:
        print("Contact is not found")


contactbook = {'Arun': 999999, 'Ben':888888}
delete_contact()
print(contactbook)