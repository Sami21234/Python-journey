
# oop(Object Oriented  Programming)
# oops concept focuses on using reusable code (DRY Principle)-(Do not repeat yourself) 

# Basic examples
# creating a class
class Employee:
    language = "Python"         # Class Attributes
    salary = 1200000            # Class Attributes


# Creating Object
sami = Employee()
sami.name = "Sami"             # Instance (Object) Attribute by using (.)
print(sami.name , sami.language, sami.salary)

ash = Employee()
ash.name = "Ash Ketchum"
print(ash.name, ash.language, ash.salary)

# Here language and salary are class Attribute, and name is Instance (object) attribute
# Note: Instance attributes, take preference over class attributes during assignment & retrieval.

# example -->

# creating class
class Student:
    name = "Sami"
    branch = "Computer Science"
    year = "3rd"
    duration = "4 years"
    location = "Mumbai"

# creating objects

obj1 = Student()
Student.name = "Mohd Sami"
print(obj1.name, obj1.branch, obj1.location)     # So, here name will be printes as Mohd Sami, cause the name attribute is an Instance attribute and has higher preferences over the class attributes
