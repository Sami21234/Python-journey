
# 7. Write a program to find out whether a given post is talking about “Python” or not. 

post = input("Enter a post: ")

if("Python".lower() in post.lower()):               # .lower() converts the string into the lowercase
    print("This post is talking about Python")

else:
    print("This post is talking Something about else")