
# 4. Write a program to find whether a given username contains less than 10 characters or not. 

user_name = input("Enter your userName: ")

if(len(user_name)<10):
    print("The Characters are less than 10")

else:
    print("More than 10 characters in the name")