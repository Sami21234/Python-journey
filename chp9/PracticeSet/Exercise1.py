
# 1. Write a program using functions to find greatest of three numbers. 
def findGreatest():
    a = int(input("Enter a number: ")) 
    b = int(input("Enter a number: ")) 
    c = int(input("Enter a number: ")) 
    if(a>b and a>c):
        print(f"The Greatest is {a}")
    elif(b>a and b>c ):
        print(f"The Greatest is {b}")
    else:
        print(f"The greatest is {c}")
findGreatest()