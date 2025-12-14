# EXCEPTION HANDLING IN PYTHON

# There are many built-in exceptions which are raised in python when something goes wrong. 
# Exception in python can be handled using a try statement. The code that handles the exception is written in the except clause. 

# As a programmer the very last way is crashing the program, So instead of getting error we can show the error messages not error by crashing, So we use try Except
# When the exception is handled, the code flow continues without program interruption. (here priting thankyou)


try:
    a = int(input("Enter a number: ")) 
    print(a)

except Exception as e:
    print(e)
print("Thankyou")

# SO, without try and except the program should be crashed and the exceution should be stopped

# We can also specify the exception to catch like below: 

try:
    a = 2/0

except ZeroDivisionError as z:
    print(z)


# RAISING EXCEPTIONS 
# We can raise custom exceptions using the ‘raise’ keyword in python. 

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(f"The division of a/b is {a/b}")
#  ZeroDivisionError: division by zero, this will throw this error 

# so, we can raise an exception in advance after creation of the b, like this

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if(b == 0):
    raise ZeroDivisionError("Hey this program is not meant to be divided by Zero(0)")
else:
    print(f"The division of a/b is {a/b}")

# TRY WITH ELSE CLAUSE  
# Sometimes we want to run a piece of code when try was successful,So we use try with else caluse. 

try:
    a = int(input("Enter a number: "))
    print(a)
except Exception as e:
    print(e)

else:
    print("I am Inside else")

# TRY WITH FINALLY 
# finally is executed always 
# It's main usage is used in function

try:
    a = int(input("Enter a number: "))
    print(a)

except Exception as e:
    print(e)

finally:
    print("I am inside finally")

# and when working with function
def main():
    try:
        a = int(input("Enter a number: "))
        print(a)

    except Exception as e:
        print(e)

    finally:
        print("I am inside finally")

main()