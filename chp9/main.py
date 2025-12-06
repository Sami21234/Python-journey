# Funnctions
# A function is a group of statements performing a specific task. 
# when the programs gets bigger than it is not good practice to write all the logics in the same function, then functions are used to write seperate logics which is reusable.

def avg():
    a = int(input('Enter your number: '))
    b = int(input('Enter your number: '))
    c = int(input('Enter your number: '))

    average = (a+b+c)/3
    print(average)

# avg()    # function call
# avg()    # function call

# Quick Quiz:  Write a program to greet a user with “Good day” using functions. 
def greet():
   name =  input("Enter your name: ")
   print(f"Hello {name} have a Good day!")
# greet()
# print("Thankyou!")

# Types of Functions
# 1. Built in function (Already present in python)
# Examples of built in functions includes len(), print(), range() etc. 

# 2. User defined functions (Defined by the user) 

# FUNCTIONS WITH ARGUMENTS 

# A variable which is passed to the function enclosed in the parentheisis
def greet(name,ending):
    print("Hello " + name)
    print(ending)
greet("Sami", "Thankyou")
greet("Ash", "Thankyou")
greet("Brock", "Thankyou")

# (return value) in the function

def greet(name):
    print("Good Day, "+ name)
    return "ok"

# a = greet("Sami")
# print(a)        # returns the none if not use return keyword above but now returns ok

# Default Parameters
# parameters are used to pass the value of the variable in the function call as by default value in the parameter

def greet(name,end = "Thankyou!"):
    print("Good Day, "+ name)
    print(end)  # here the end parameter has default value as thankyou 

greet("Sami")

# def greet(name,end):
#     print("Good Day, "+ name)
#     print(end)  # here the end parameter has no default value and doesnot specified the value in the arguments

# greet("Sami")      # throws an error