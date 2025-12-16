
# 5. Write a program to find the maximum of the numbers in a list using the reduce function. 
from functools import reduce
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20, 45, 23]

def greater(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater, a))