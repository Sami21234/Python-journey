# Loops

# Sometimes we want to repeat a set of statements in our program. For instance:  Print 1 to 1000. 
# Loops make it easy for a programmer to tell the computer which set of instructions to repeat and how! 

# There are two types of loops in python
# while loop
# for loop

# while loop
# while loop checks the condition first, if it is true, then the body of the  while loop is executes.

i = 1
while(i < 6):
    print(i)
    i += 1

# Quick Quiz:  Write a program to print the content of a list using while loops. 

list1 = ["Apple", "Banana", "Cherry", "Kiwi", "Mango", "Grapes"]

i = 0

while(i < len(list1)):
    print(list1[i])
    i += 1

# for loop

# A for loop is used to iterate through a sequence like list, tuple, or string [iterables] 

# The range() function in python is used to generate a sequence of number. 


for i in range(5):  # prints the n-1 numbers here
    print(i)

# step-size in for loop 
# It is used to skip the range of values specified in the step_size

for i in range(0, 41, 4):
    print(i)

# We can iterate the list, tuple or string in the python using for loop

# For loop with List
list1 = ["Mohd Sami", "Apple", "Banana", "Cherry", "Ash"]

for item in list1:
    print(item)

# For loop with tuple
t1 = ("Mohd Sami", 4, 45, 567)
for item in t1:
    print(item)

# For loop with else
# else statement can be implemented in the for loop, until the for loop gets the value it will iterate and once the for loop does'nt get the value it will execute the else statment

l = [1,2,3,4,5]
for item in l:
    print(item)
else:
    print("Done")    # this is printed when the loop exhausts! 

# Break Statement
# ‘break’ is used to come out of the loop when encountered. It instructs the program to – exit the loop now. 

for i in range(0,81):
    if (i ==5):
        break        # Exit the loop right now
    print(i)

# Continue Statement
# ‘continue’ is used to stop the current iteration of the loop and continue with the next one. It instructs the Program to “skip this iteration”. 

for i in range(0,11):
    if (i ==5):
        continue        # Skip this iteration
    print(i)

# Pass Statement
# pass is a null statement in python. 
# It instructs to “do nothing”. 

for i in range(0, 16):
    pass

# Suppose, we want now to only do operation using while and iteration later using for loop then we, can use the pass statement in the for loop for not getting an error

i = 0
while(i < 11):
    print(i)
    i += 1