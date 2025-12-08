# OTHER METHODS TO READ THE FILE. 

# 1. readlines() and readline()  reads the files in the list form

f = open("file.txt")
lines = f.readlines()
print(lines, type(lines))
f.close()

# MODES OF OPENING A FILE 
'''
r – open for reading 
w - open for writing  
a - open for appending 
+  - open for updating. 
‘rb’ will open for read in binary mode. 
‘rt’ will open for read in text mode. 

'''
# append (a) - used to add at the end of the string in the file

st = "Hey another line\n"
f = open("write.txt","a")
f.write(st)
f.close()