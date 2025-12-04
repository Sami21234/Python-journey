# CONDITIONAL EXPRESSION :
# Used when working with certain conditions,
# Conditionals are if-else, elif


# if-else:-

a = int(input("Enter your age: "))

if(a>=18):
    print("You are free to drive")

else:
    print("You  are a child, Have Some milk!")

# if elif else ladder :-

b = int(input("Enter your Age: "))

if(b>=18):
    print("You are Eligible for voting")

elif(b==0):
    print("Invalid Age")

elif(b<0):
    print("Age cannot be neagtive")

else:
    print("You are a Giga Chad, Have some milk!")


# Quick Quiz: Write a program to print yes when the age entered by the user is greater than or equal to 18. 

age = int(input("Enter your Age: "))

if(age>=18):
    print("Yes")

elif(age<0):
    print("Invalid Age, Age cannot be negative")

else:
    print("No")

# Multiple if statements

age = int(input("Enter your Age: "))

# If Statement 1
if(age%2 == 0):
    print("Age is even")
# If statement 1 is ended and will work independently

# If Statement 2
if(age>=18):
    print("Yes")

elif(age<0):
    print("Invalid Age, Age cannot be negative")

else:
    print("No")
# If statement 2 is ended and will work independently