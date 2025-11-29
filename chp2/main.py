# Variables and Data Types

# Variables are containers for storing data values
a = 1
b = True
c = "Sami"
d = None

print(a,b,c,d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Data Types
'''
Data types represents the type of data stored in the variable
for example --> int, float, str, bool, NoneType

'''
# Lists
'''
Lists are the collection of the  Data of the different data types seperated by columns and enclosed with the Square Brackets, and there can be nested lists in the Main List.
They are mutable (can be changed after creation)
'''

list1 = [8, 2.5, [-4,"Sami"], ["Sami", "Siddiqui"]]
print(list1)

# Tuples
'''
Tuples are the collection of the  Data of the different data types seperated by columns and enclosed within the parentheses. 
They are immutable (cannot be changed after creation) 
'''

tuple1 = [8, 2.5, [-4,"Sami"], ["Sami", "Siddiqui"]]
print(tuple1)

# Dictionary
'''
Dictionary are the collection of the unorderd data containing a key:value pairs, The key:value pairs are enclosed within a curly braces

'''
dict1 = {
    "Name":"Mohd Sami", "Age":20, "Occupation":"Developer"
}
print(dict1)