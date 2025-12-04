
# 5. Write a program which finds out whether a given name is present in a list or not. 

list1 = ["Sami", "Ash", "Brock", "Kai", "Tyson"]
# print(type(list1))
name = input("Enter your Name: ")
if(name in list1):
    print("Name is present in the List")

else:
    print("Name is not present in the list")