
# SELF PARAMETER
# self refers to the instance of the class. It is automatically passed with a function call from an object. 

class Employee:
    language = "Python"         # Class Attributes
    salary = 1200000            # Class Attributes

    def getInfo(self):
        print(f"The Language is {self.language}. The salary is {self.salary}")


# Creating Object
sami = Employee()
sami.language = "JavaScript"              # Instance (Object) Attribute
# print(sami.name , sami.language, sami.salary)
sami.getInfo()        # so, here this gives one arguments which is not given in the above functions, so we can give the self as function call
# same as
# Employee.getInfo(sami)   ---> same output


# STATIC METHOD 
# Sometimes we need a function that does not use the self-parameter. We can define a static method like this: 
# for example :-
class Student:
    name = "Mohd Sami"
    salary = 12000000

    @staticmethod
    def getSalary():          # without self passing using static method
        print("Good Morning")

sami = Student()
sami.salary = 20000000
sami.getSalary()


# __INIT__() CONSTRUCTOR 
'''
__init__() is a special method which is first run as soon as the object is created. 
__init__() method is also known as constructor. 
It takes ‘self’ argument and can also take further arguments. 

'''
# for example --->

class Employee:
    name  = "Sami"
    language = "Python"
    salary = 12000000

    def __init__(self, name,salary, language):         # dunder method which is automatically called without calling the function at the end and can also takes further arguments
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

sami = Employee("Sami", 1200000, "JavaScript")
# sami.name = "Mohd Sami"
print(sami.name, sami.salary, sami.language)

