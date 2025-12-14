# # Advance Python Concepts 

# # NEWLY ADDED FEATURES IN PYTHON 

# # 1. Warlus Operator (:=)
# # It is convineance method, shorter way to both assign and comparing like :-

# # Using walrus operator 
# if (n := len([1, 2, 3, 4, 5])) > 3:
#     print(f"List is too long ({n} elements, expected <= 3)")

# # Output: List is too long (5 elements, expected <= 3) 

# # 2. type defination
# # Type hints are added using the colon (:) syntax for variables and the (->) syntax for function return types.

# n : int = 5
# n.imag  # we can get all the methods of the explicitly defined variable types using type defination here ( : int)

# name : str = "Sami"
# print(name.swapcase())    # we can get all the methods of the explicitly defined variable types using type defination here ( : str)

# # for the function we use (->)

# def sum(a:int, b:int) -> int:
#     return a + b
# print(sum(2, 2))

# # this methods are used by the programmers, If other person is working on the code then they can easily understand work with the data by knowing the type


# # MATCH CASE

# # Python 3.10 introduced the match statement, which is similar to the switch statement found in other programming languages.   
# # The basic syntax of the match statement involves matching a variable against several cases using the case keyword. 

# def http_status(status):
#     match status:
#         case 200:
#             return "OK"
#         case 404:
#             return "Not FOund"
#         case 500:
#             return "Internal Server Error"
#         case _:
#             return "Unknown status"

# print(http_status(200))
# print(http_status(500))
# print(http_status(404))
# print(http_status(407))


# # DICTIONARY MERGE & UPDATE OPERATORS 
# # we can merge and update the dictionaries in this method
# # using the operator like | and |=

# dict1 = {'a' : 1, 'b' : 2}
# dict2 = {'b' : 3, 'c': 4}
# dict1 |= {'a' : 2, 'b' : 2}  # updating the dictionary
# merged = dict1 | dict2
# print(merged)

# #  Multiple context managers
# # You can now use multiple context managers in a single with statement more cleanly using the parenthesised context manager 
# # for example-->


# with (
#     open('file1.txt') as f1,
#     open('file2.txt') as f2
# ):
#     # process the file
#     pass

# with this method we can process multiple files at a time


# THE GLOBAL KEYWORD
# ‘global’ keyword is used to modify the variable outside of the current scope. 

a = 45      # global variable

def fun():
    global a    # this will change the global variable value
    a = 3       #local variable of the function 
    print(a)
fun()
print(a)

# ENUMERATE FUNCTION
# The ‘enumerate’ function adds counter to an iterable and returns it 

l = [3, 45, 567, 2435]
# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1

# This can be simplified by  ENUMERATE FUNCTION

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")

# LIST COMPREHENSIONS 
# List Comprehension is an elegant way to create lists based on existing lists. 

# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = []
# for item in list1:
#     if(item>7):
#      list2.append(item)

# print(list2)

# By list comprehension method

list1 = [1,2,3,4,5,6,7,8,9,10]

list2 = [item for item in list1 if item>7]
print(list2)