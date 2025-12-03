# Dictionary

# It is used to store the data in the form of (key:value) pairs and enclosed in the curly brackets {}

a = {}       # Empty Dictionary

professions = {
    "Sami": "Developer and Software Engineer",
    "Ash Ketchum": "Pokemon Master",
    "Brock": "Pokemon Breeder",
    "Harry": "One Man Army"
}

print(professions, type(professions))
print(professions["Sami"])

# Dictionary Methods

# 1. .items() --> returns the list of key:value tuples

marks = {
    "Sami": 95,
    "Ash": 92,
    "Brock":90
}

print(marks.items())

# 2. .keys() --> returns the list of the dictionary keys

marks = {
    "Sami": 95,
    "Ash": 92,
    "Brock":90
}

print(marks.keys())
print(marks.values())

# 3. update() -->  Updates the dictionary with new key-value pairs. 

marks = {
    "Sami": 99,
    "Ash": 92,
    "Brock":90,
    0: 0
}

marks.update({"Sami":99})
print(marks)

# 4. .get()

# : Returns the value of the specified keys (and value is returned eg."harry" is returned here).
# It returns the value if present and if not present then returns (None)

marks = {
    "Sami": 99,
    "Ash": 92,
    "Brock":90,
    0: 0
}

Get = marks.get("Sammmi")
print(Get)

# Difference between get and [] often asked in the interview

# print(marks.get("Sammi")) # Prints None
# print(marks["Sammi"]) # Returns an Error

# Sets in python
# Sets  are unordered collection of the unique elements,It contains only the non-repated elements, They are also enclosed in the {}
# They are immutable, and can't access the element using the indexing.
# It contains the multiple datatypes in the set.

# To make empty set 
# e = set()

s = {1,2,2,34,5}
print(s)

m = {1,2,3,4,5,6,7,"Sami",True,False}
print(m,type(m))

# Sets Methods
# 1. .add() ---> used to add the element in the set

m = {1,2,3,4,5,6,7,"Sami"}
m.add("Developer")
print(m)

# 2. .len() ---> returns the length of the set
print(len(m))

# 3. .remove() ----> used to remove the elements from the sets
m.remove("Sami")
print(m)

# 4. .clear() ---> used to clear (Empty) the set
m.clear()
print(m)


# 5. .union() ---> It used to get all the elements from the both the sets

s1 = {1,2,4,5,6}
s2 = {1,2,4,5,6,6,7,8,8,9,9,99,0,6,3,7}
print(s1.union(s2))

# 6. .intersection() ---> It used to get the common elements from both the sets

print(s1.intersection(s2))

# issuperset
print(s2.issuperset(s1))

# issubset
print({1,3,5}.issubset(s2))