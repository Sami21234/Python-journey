# # FILE I/O 

# # Python has a lot of functions for reading, updating, and deleting files.



# # for reading the file 
# # OPENING A FILE 
# # Python has an open() function for opening files. It takes 2 parameters:  filename and mode. and by-default mode is read(r)
# f = open("file.txt", "r")        # open the file for reading or writing
# data = f.read()
# print(data)
# f.close()          # close the file (important step) 



# # WRITE FILES IN PYTHON 

# str = "Heyy, this string is used for writing the file function and creating the file dynamically"

# f = open("write.txt", "w")
# f.write(str)
# f.close()

# f = open("write.txt")
# data = f.read()
# print(data)
# f.close()

# with statement - used for automatically close the file without writing the f.close()

with open("file.txt","r") as f:
    print(f.read())
    
