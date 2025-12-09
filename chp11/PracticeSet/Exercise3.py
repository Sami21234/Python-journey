
# 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute? 

class Student:
    # class Attributes
    a = "This is a class Attribute"
    name = "Sami"
    year = 3
    branch = "Cse-AIML"

# creating the object
obj1 = Student()
print(obj1.a)           # Prints a class attributes because instance attribute is not present
obj1.a = 0              # Prints the instance attribute because instance attribute is present
print(obj1.a)           # Prints the class attribute

# So, NO the class Attribute will not be changed 

