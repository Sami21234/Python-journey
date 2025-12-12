
# 1. SUPER() METHOD  

class Parent:
    def __init__(self):
        print("Constructor of Parent")
    a = 1

class  Child1(Parent):      # Child class of the Parent class
    def __init__(self):
        print("Constructor of Child1")
    b = 2

class Child2(Child1):       # Child of the Child1
    def __init__(self):
        super().__init__()
        print("Constructor of Child2")
    c = 3

# object
# o = Parent()
# print(o.a) # Prints the a attribute
# # print(o.b) # Shows an Error as there is no b attribute in Parent class

# o = Child1()
# print(o.a, o.b) # Prints the a and b attribute as it is the inherited class from parent class

o = Child2()
print(o.a, o.b, o.c)

# But sometimes we need to access the methods of the super(parent class) in the derived class so we use Super() method


# 2. CLASS Method

# A class method is a method which is bound to the class and not the object of the class. @classmethod decorator is used to create a class method. 
# In this method the value contains of the class attribute not the instance attribute

# class Employee:
#     a = 1

#     @classmethod
#     def show(cls):
#         print(f"The value of the class attribute is {cls.a}")

# e = Employee()
# e.a = 45
# e.show()


# 3. @PROPERTY DECORATORS 

class Student:
    a = 1

    @classmethod
    def show(cls):
        print(f"The value of the class attribute is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Student()
e.a = 45
e.name = "Mohd Sami"
print(e.fname, e.lname)   # Internally calling the name() function 
e.show()


# OPERATOR OVERLOADING IN PYTHON  
# Operators in Python can be overloaded using dunder methods. 
# These methods are called when a given operator is used on the objects. 

class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    
n = Number(1)
m = Number(2)

print(n+m)