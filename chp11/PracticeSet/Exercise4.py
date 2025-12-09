
# 4. Add a static method in problem 2, to greet the user with hello. 

class Calculator:
    def __init__(self, n):
        self.n = n

    @staticmethod                   # Static method decorator
    def greet():
        print("Hello User!")

    def square(self):
        print(f"The Square of the {self.n} is {self.n * self.n}")

    def cube(self):
        print(f"The Cube of the {self.n} is {self.n * self.n * self.n}")

    def squareRoot(self):
        print(f"The SquareRoot of the {self.n} is {self.n**1/2}")

a = Calculator(4)
a.greet()
a.square()
a.cube()
a.squareRoot()
