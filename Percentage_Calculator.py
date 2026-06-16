subject1 = float(input("Enter marks of Subject 1: "))
subject2 = float(input("Enter marks of Subject 2: "))
subject3 = float(input("Enter marks of Subject 3: "))
subject4 = float(input("Enter marks of Subject 4: "))
subject5 = float(input("Enter marks of Subject 5: "))

total = subject1 + subject2 + subject3 + subject4 + subject5

maximum_marks = 500

percentage = (total / maximum_marks) * 100

print("Total Marks =", total)
print("Percentage =", percentage, "%")
