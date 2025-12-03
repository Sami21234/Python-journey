
# 7. If the names of 2 friends are same; what will happen to the program in problem 6? 

d1 = {}     #Empty dictionary

name = input("Enter your name: ")
lang = input("Enter your favorite language: ")

d1.update({name:lang})

name = input("Enter your name: ")
lang = input("Enter your favorite language: ")

d1.update({name:lang})

name = input("Enter your name: ")
lang = input("Enter your favorite language: ")

d1.update({name:lang})

name = input("Enter your name: ")
lang = input("Enter your favorite language: ")

d1.update({name:lang})

print(d1)

# So, if the Keys are repeated then the current one which is written is printed, the previous one is not printed and  updated to the current one
