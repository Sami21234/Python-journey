# INHERITANCE & MORE ON OOPS

# Inheritance is a way of creating a new class from an existing class. 

class Employee:             # Base Class
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.showLanguage} language")

# a = Employee()
# b = Programmer()
# print(a.company, b.company)
# But this is not efficient for passing the methods and instances from one class to another class

# so instead of doing this we can use inheritance

class Programmer(Employee):         # Derived (Inherited) Class
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.showLanguage} language")

a = Employee()
b = Programmer()
print(a.company, b.company)

