import os
mypath = "/Users/shinysuresh/Documents/Projects_pycharm/KCGBridgeCourse/"
print(os.listdir(mypath))
for (root, directories, files) in os.walk(mypath):
    for name in files:
        if name.endswith(".py"):
            print(os.path.join(root, name))
    for name in directories:
        print(os.path.join(root, name))
