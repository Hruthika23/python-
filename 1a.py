
name = input("Enter Name: ")
dob = input("Enter DOB: ")
usn = input("Enter USN: ")
dept = input("Enter Department: ")


m1 = float(input("Enter marks for subject 1: "))
m2 = float(input("Enter marks for subject 2: "))
m3 = float(input("Enter marks for subject 3: "))
m4 = float(input("Enter marks for subject 4: "))
m5 = float(input("Enter marks for subject 5: "))


total = m1 + m2 + m3 + m4 + m5
percentage = total / 5


print("\n Student Details ")
print("Name:", name)
print("DOB:", dob)
print("USN:", usn)
print("Department:", dept)

print("\nMarks:", m1, m2, m3, m4, m5)
print("Total Marks:", total)
print("Percentage:", percentage, "%")


if percentage >= 90:
    print("Grade: Excellent")
elif percentage >= 75:
    print("Grade: Very Good")
elif percentage >= 60:
    print("Grade: Good")
elif percentage >= 50:
    print("Grade: Pass")
else:
    print("Grade: Fail")