# Strings
# Anything that Enclosed in the Single or Double Quotes is Called String
# Strings are the Datatypes which contains the Words or letters or textual Data

name = "Sami"
Age = 20

print("Heyy, " + name)
print("He said, 'I want to eat an Apple'.")

# Multiple line Strings

a = """
Heyy, My name is Sami
I am Web Developer
I am Pursuing Engineering in Computer Science.
    """
print(a)

# Accessing the Character of a String
# In python, the Strings are like an Array, So we can access them using there indexes enclosed in the Square Brackets

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print('\n')

# Looping through the Strings
# We cannot manually access the each element of an array of Strings in the large data so we loop through the Strings using the for loop

for letters in name:
    print(letters)

# Slicing in Strings
# Slicing are used to get the part of the sring

strName = "Mohd Sami"
slicing = strName[1:6]
print(slicing)
print(strName[:2])
print(strName[0:])

# Slicing with skip values
# We can provide a skip value as a part of our slice like this:
 
word = "Amazing"
print(word[1:6:3])  # last indexing is the skip values or indexes

# String Functions

# 1. len() --> this function is used to find the entire length of the string

str = "Ash Ketchum"
print(len(str))

# 2. endswith()
# this function is used to check whether the string ends with a particular word stated by the user and returns the boolean value

str = "Ash Ketchum"
print(str.endswith("chum"))

# 3. startswith
# Same as endswith but state the startinig word

# 4. count()
# this function is used to find the count of the particular element described by the user

str = "Ash Ketchum"
str1 = str.lower()
print(str1.count("s"))

# 5. capitalize()
# used to create the first letter of the words in capital

str = "ash ketchum"
print(str.capitalize())

# 6. find()
# this function is used to find the word and returns the index of the first occurence of that word in the string

str = "Ash Ketchum"
print(str.find("h"))

# 7. replace()
# This function is used to rplace the old word with a new word in the entire string

str = "Ash Ketchum is a Pokemon master."
print(str.replace("master","trainer"))

