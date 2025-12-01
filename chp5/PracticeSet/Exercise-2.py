# 2. Write a program to accept marks of 6 students and display them in a sorted manner. 

marks = []

stu1 = int(input("Enter your Marks:"))
marks.append(stu1)

stu2 = int(input("Enter your Marks:"))
marks.append(stu2)

stu3 = int(input("Enter your Marks:"))
marks.append(stu3)

stu4 = int(input("Enter your Marks:"))
marks.append(stu4)

stu5 = int(input("Enter your Marks:"))
marks.append(stu5)

stu6 = int(input("Enter your Marks:"))
marks.append(stu6)

marks.sort()
print(marks)