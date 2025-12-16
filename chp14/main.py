#   ADVANCED PYTHON 2 
from functools import reduce        # for reduce function
# 1. VIRTUAL ENVIRIONMENT 

# An environment which is same as the system interpreter but is isolated from the other Python environments on the system. 

# INSTALLATION 
# To use virtual environments, we write: 
# pip install virtualenv            # Install the package 

# We create a new environment using: 

# virtualenv myprojectenv           # Creates a new venv 

# The next step after creating the virtual environment is to activate it. 
# .\env\Scripts\activate.ps1

# We can now use this virtual environment as a separate Python installation. 

# And for deactivation of the Virtual Environment 
# deactivate   (command)


# 2. LAMBDA FUNCTIONS 

# Function created using an expression using ‘lambda’ keyword. 

# def square(n):
#     return n*n
# print(square(5))

# we can do this by lambda function as 
square = lambda x: x*x
print(square(6))

# 3. JOIN Methods (Strings)
# Creates a string from iterable objects.

a = ["Sami", "23", "Ash", "Brock"]
# and suppose we want to separate the list by "-" we use join method
final = "-".join(a) 
print(final)

# FORMAT METHOD (STRINGS) 
# Formats the values inside the string into a desired output. 
# But we rarely used this due to f string

s = "{} is a good {}".format("Sami", "boy")  
s = "{1} is a good {0}".format("Sami", "boy")   # boy is a good Sami (due to indexing)
print(s)

# 4. MAP, FILTER & REDUCE

# Map:-
# Map applies a function to all the items in an input_list. 

l = [1, 2, 3, 4, 5, 6, 7, 8]
square = lambda x:x*x
# Now we can use the  map method to get the squared list of the list
squarList = map(square, l)  # syntax: map(function, iterable)
print(list(squarList))

# Filter:-
# Filter creates a list of items for which the function returns true. 
# means it selects elements based on the condition

def even(n):
    if (n%2 == 0):
        return True
    return False
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
onlyEvenList = filter(even, list1)
print(list(onlyEvenList))

# Reduce:-
# It combines all values into one
# It is functiontool

def sum(a, b):
    return a + b
mul = lambda x,y:x*y

print(reduce(sum, l))
print(reduce(mul, l))