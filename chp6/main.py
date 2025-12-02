# Dictionary

# It is used to store the data in the form of (key:value) pairs

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

print(marks.get("Sammi")) # Prints None
print(marks["Sammi"]) # Returns an Error

