
# 9. Write a program to find out whether a file is identical & matches the content of another file. 

with open("this.txt") as f:
    content1 = f.read()

with open("poems.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes! this files are identicsl")
else:
    print("No these files are not identical")