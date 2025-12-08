
# 7. Write a program to find out the line number where python is present from ques 6. 
line = 1
with open("log.txt","r") as f:
    lines = f.readlines()

lineNo = 1
for line in lines:
    if("python" in line):
        print(f"Yes! python is present in the Line Number: {lineNo} in the log file")
        break
    lineNo += 1
else:
    print("Python is not present")