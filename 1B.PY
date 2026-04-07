
name = input("Enter name: ")
yob = int(input("Enter year of birth: "))

current_year = 2026

age = current_year - yob

print("\nName:", name)
print("Age:", age)

if age >= 60:
    print("Status: Senior Citizen")
else:
    print("Status: Not a Senior Citizen")