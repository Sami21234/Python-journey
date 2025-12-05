
# 7. Write a program to print the following star pattern. 
#   * 
#  *** 
# ***** for n = 3 

n = int(input("Enter the number: "))
for i in range(1, n+1):
    print(" "* (n-i), end="")  # for spcaing and (end="") is for not providing the space by-default by print
    print("*"* (2*i-1), end="")  # for star odd Stars-->(2*i -1)
    print("")