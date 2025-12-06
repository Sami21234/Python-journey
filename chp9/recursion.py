# Rercursion

# Recursion is a function which calls itself
# It is used to directly use a mathematical formula as function.  

# Best example of understanding the recursion is Factorial
# Logic of the factorial

# factorial(n) = n * factorial(n-1)

def factorial(n):

    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)
n= int(input("Enter a number: "))
print(f"The factorial of {n} is : {factorial(n)}")
