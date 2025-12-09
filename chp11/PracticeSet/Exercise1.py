
# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft. 

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Mohd Sami",12000000, 400097)
print(p.name, p.salary, p.pin, p.company)

s = Programmer("Ash Ketchum",12000000, 400097)
print(s.name, s.salary, s.pin, s.company)