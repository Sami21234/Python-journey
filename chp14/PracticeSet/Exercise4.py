
# 4. Write a program to filter a list of numbers which are divisible by 5. 

def divisbleBy5(n):
    if(n%5 == 0):
        return True
    return False
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 20, 45, 23]
onlyDiviBy5 = filter(divisbleBy5, list1)
print(list(onlyDiviBy5))
