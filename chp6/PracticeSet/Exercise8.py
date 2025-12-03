# # 8. If languages of two friends are same; what will happen to the program in problem 6? 

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

# So, if the values are repeated, it doesnot matters, it will print the values 
# {'Sami': 'Python', 'Ash': 'Js', 'Brock': 'js', 'Harry': 'Python'}