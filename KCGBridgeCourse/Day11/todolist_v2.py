'''
Todolist using files for storage
'''

def read_file():
    tasks = []
    with open("task.txt", "r") as reader:
        line = reader.readline()
        while line != '':
            tasks.append(line.strip('\n'))
            line = reader.readline()
    return tasks


def write_file(tasks):
    with open("task.txt", "w") as writer:
        for line in tasks:
            writer.write(line + "\n")


def add_item():
    item = input("Enter the new item:")
    todolist.append(item)


def remove_item():
    item = input("Enter the item to be removed: ")
    todolist.remove(item)


todolist = read_file()
print(todolist)
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
write_file(todolist)
