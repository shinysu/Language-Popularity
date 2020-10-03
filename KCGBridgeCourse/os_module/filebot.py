import os
import datetime

file_data ={}
todays_date = datetime.date.today()

def get_all_files():
    for (root, directories, files) in os.walk(filepath):
        for name in files:
            file = os.path.join(root, name)
            print(file)

def files_by_extension():
    extension = input("Enter the file extension: \n").strip('.')
    for (root, directories, files) in os.walk(filepath):
        for name in files:
            if name.endswith(extension):
                file = os.path.join(root, name)
                print(file)

def files_created_yesterday():
    start_date = todays_date - datetime.timedelta(days=1)
    end_date = todays_date
    get_files_by_date(start_date, end_date)

def files_between_date():
    #todo - date validation
    try:
        start_date = convert_to_date(input("Enter the start date (yyyy-mm-dd): "))
        end_date = convert_to_date(input("Enter the end date (yyyy-mm-dd): "))
        get_files_by_date(start_date, end_date)
    except:
        print("Invalid date")

def get_files_by_date(start_date, end_date):
    for (root, directories, files) in os.walk(filepath):
        for name in files:
            file = os.path.join(root, name)
            created_date = get_created_date(file)
            if check_file_in_range(created_date, start_date, end_date):
                print(file, "\t", created_date)

def check_file_in_range(created_date, start_date, end_date):
    if start_date <= created_date and created_date <= end_date:
        return True
    else:
        return False

def get_created_date(file):
    return datetime.date.fromtimestamp(os.path.getctime(file))

def convert_to_date(x):
    year, month, day = map(int, x.split('-'))
    return datetime.date(year, month, day)

def check_latest(createdDate):
    createdDateLimit = createdDate + datetime.timedelta(days=1)
    if createdDateLimit > todaysDate:
        return True
    else:
        return False

file_options = {1: get_all_files, 2: files_by_extension, 3:files_created_yesterday, 4:files_between_date}
print("Hello! I am a file-finder bot! I can find you files in your machine")
while True:
    print("What would you like to search?")
    try:
        option = int(input("Type your option\n0 --> quit\n1 --> Display all files in directory\n2 --> Search by filetype\n"
                           "3 --> Get files created yesterday\n4 --> Get files between date\n"))
        if option == 0:
            break
        elif option in file_options:
            filepath = input("Enter the file path: ").strip('"\'')
            file_options[option]()
        else:
            print("Please enter a valid option")
    except ValueError as ve:
        print("Invalid option")