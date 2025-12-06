
# 8. Write a python function to print multiplication table of a given number. 

def mul_Table(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")
mul_Table(int(input("Enter a number: ")))
