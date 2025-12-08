
# 1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’. 

f = open("poems.txt")
content = f.read()

if("twinkle" in content):
    print("This file contains the word 'twinkle'")
else:
    print("This file not contains the word 'twinkle'")
f.close()