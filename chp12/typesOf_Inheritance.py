
# Types of Inheritace
'''

• Single inheritance 
• Multiple inheritance 
• Multilevel inheritance 

'''

# 1. Single Inheritance
# Single inheritance occurs when child class inherits only a single parent class.

# Base class ---> Derived class

# 2. Multiple Inheritance
# Multiple Inheritance occurs when the child class inherits from more than one parent classes.

class Employee:             # Base Class(Parent Class)
    company = "ITC"
    salary = 120000
    def show(self):
        print(f"The name is {self.company} and the salary is {self.salary}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Your favourite programming language is {self.language}")

class Programmer(Employee, Coder):         # Derived (Inherited) Class
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")

a = Employee()
c = Coder()
b = Programmer()
# print(a.company, b.company, b.language)
b.show()
b.printLanguage()
b.showLanguage()

# 3. MULTILEVEL INHERITANCE
#  When a child class becomes a parent for another child class.

class Parent:
    a = 1

class  Child1(Parent):      # Child class of the Parent class
    b = 2

class Child2(Child1):       # Child of the Child1
    c = 3

# object
o = Parent()
print(o.a) # Prints the a attribute
# print(o.b) # Shows an Error as there is no b attribute in Parent class

o = Child1()
print(o.a, o.b) # Prints the a and b attribute as it is the inherited class from parent class

o = Child2()
print(o.a, o.b, o.c)
