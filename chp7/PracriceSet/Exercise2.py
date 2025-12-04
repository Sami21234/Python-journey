
# 2. Write a program to find out whether a student has passed or failed if it requires a  total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user. 

sub1 = int(input("Enter the Marks of the English Subject: "))
sub2 = int(input("Enter the Marks of the Math Subject: "))
sub3 = int(input("Enter the Marks of the Science Subject: "))

# Check for total percentage

total_precentage = ((sub1 + sub2 + sub3)*100)/300

if(total_precentage>=40 and sub1>=33 and sub2>=33 and sub3>=33):
    print(f"You are Pass: {total_precentage}%")

else:
    print(f"You are Fail! {total_precentage}%")
