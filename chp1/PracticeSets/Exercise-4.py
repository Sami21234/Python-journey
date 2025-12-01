# 4. Write a python program to print the contents of a directory using the os module. 
# Search online for the function which does that. 

import os

# You can change this to any directory you like
directory = "/"

try:
    entries = os.listdir(directory)
    print(f"Contents of directory '{directory}':")
    for entry in entries:
        print(entry)
except Exception as e:
    print(f"Error: {e}")
