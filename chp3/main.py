# Operators
# They are the  special symbols used to perform specific operations

# 1. Arithmetic opertors
print(5+6)
print(5-6)
print(5*6)     # Multiplication
print(5/6)     # Division
print(5//6)    # Floor Division
print(5%3)     # Modulus 
print(3**3)    # Exponential

# 2. Assignment operators

x = 5-3
print(x)
y = 5
y -= 2
print(y)

# 3. Compoarison operator (Returns the true or false as an output)

w = 5<4
print(w)

e = 5<=5
print(e)

# 4. Logical operators

r = True and False
v = True or False
m = not True

print(r,v,m)

# TypeCasting

'''
TypeCasting is the conversion of the one data type to the other data type in Python

'''

# Explicit TypeCasting
a = "4"
b = "5"

print(int(a) + int(b))

string = "15"
number = 7

str_number = int(string)
sum = str_number + number
print(sum)

# Implicit  TypeCaasting (Lower order type is converted into the higher orders data type here int ---> float)

c = 1.9
d = 8
print(c+d)

# Taking UserInput in python

# name = input("Enter your name : ")
# print("My name is ",name)

# Python will always takes the input value as string so we have to convert those into the suitable types as requirement
x = input("Enter a first number :")
y = input("Enter a second number :")

print(x+y)
# output : 12300

print(int(x)+int(y))
# Correct output 