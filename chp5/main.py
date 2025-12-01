# Lists 
# They are the order collection of the data of any data types, sperated by the comma (,) and enclosed in the []
# they are mutlable 

list1 = ["Apple",72,True,72.9,"Mohd Sami"]
print(list1)
print(list1[0])

list1[0] = "Mohd Sami"  # Mutable
print(list1[0])

# List methods

# 1. sort()  --> sort the list into the Ascendding order
list = [1,2,3,7,9,56,34,2]
list.sort()
print(list)

# 2. append() --> this method is used to add at the end of the list

list1.append("Siddiqui")
print(list1)

# 3. reverse() --> this method is used to reverse the list

list.reverse()
print(list)

# 4. insert() --> this method is used to insert the element in the list at any index

list.insert(0,99)    # Insert 99 at the index [0]
print(list)

# 5. pop() --> this method is used to delete an element from the element based on the index and writtens its value

# list.pop(1)
print(list.pop(1))    # will return the popped value
print(list)

# 6. remove() --> this method will remove the element from the list
list.remove(3)
print(list)


# Tuples
# Tuples are the collection of the data, seperated by the comma, enclosed with parentheisis.
# They are immutable

a = (1, 2, 3, 45, 67, 34, 34, 2335, "Mohd Sami")
print(a)
print(type(a))

# Tuples method

# 1. count()

numb = a.count(34)
print(numb)

# 2. index()

ind = a.index(2)
print(ind)

# 3. len()

print(len(a))