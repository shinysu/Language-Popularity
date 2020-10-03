'''
The todolist version using a list variable
'''

def add_item():
    item = input("Enter the new item:")
    todolist.append(item)

def remove_item():
    item = input("Enter the item to be removed: ")
    todolist.remove(item)

todolist = []
while True:
    print("Press\n 1 to add item \n 2 to remove item \n 3 to exit")
    choice = int(input())
    if choice == 1:
        add_item()
    elif choice == 2:
        remove_item()
    else:
        break
print(todolist)
