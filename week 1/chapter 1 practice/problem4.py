# python program to print the contents of a directory using OS module search online for the function which does that

import os

# specify the directory you want to list
path = "C:\Program Files"   # replace with your directory path

try:
    # get the list of files and directories
    contents = os.listdir(path)
    
    print(f"Contents of '{path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print(f"The directory '{path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{path}'.")

