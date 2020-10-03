import os
import datetime

filepath = "/Users/shinysuresh/Documents/"
filetype = ['document', 'text', 'presentation', 'python']
file_data ={}

def add_to_filedata(name, extension):
    if extension in file_data:
        file_data[extension].append(name)
    else:
        file_data[extension] = [name]

def get_all_files(filepath):
    for (root, directories, files) in os.walk(filepath):
        for name in files:
            extension = name.split('.')[-1]
            add_to_filedata(name, extension)

def print_file_by_extension(extension):
    for file in file_data[extension]:
        print(file)

def print_all_files():
    for type in file_data:
        print(type)
        print_file_by_extension(type)

def print_file_types():
    for type in file_data:
        print(type)

print("Hello! I am a file-finder bot! I can find you files in your machine")
filepath = input("Enter the file path: ")
get_all_files(filepath)
print("What would you like to search? Type your option")
while True:
    choice = int(input("1 --> Display all files in directory\n2 --> Search by filetype\n3 --> Search by date\n"))
    if choice == 1:
        print_all_files()
    elif choice == 2:
        print_file_types()
        type = input("Enter the filetype: ")
        print_file_by_extension(type)

