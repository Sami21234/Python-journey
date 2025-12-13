
# 7. Override the __len__() method on vector of problem 5 to display the dimension of the vector.

class Vector:
    def __init__(self, l):
        self.l = l

    # def __add__(self, other):
    #     result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    #     return result

    # def __mul__(self, other):
    #     result = self.x * other.x + self.y * other.y + self.z * other.z
    #     return result
    
    def __len__(self):
        return len(self.l)
    
    # def __str__(self):
    #     return f"Vector({self.x}, {self.y}, {self.z})"

# Test the implementation
v1 = Vector([1, 2, 3])
# print(type(v1))
print(len(v1))
