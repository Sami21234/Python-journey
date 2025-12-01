# 1. Write a Script that asks for name/age and prints: "In 5 Years,[Name] will be [Age+5]"

name = input("Enter your name: ")
age = input("Enter your age:")
newAge = int(age)
fage = newAge+5
print(f"In 5 Years, {name} will be of {fage} years old")