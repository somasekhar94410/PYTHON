basic_salary = float(input("Enter Basic Salary: "))
hra = float(input("Enter HRA: "))
da = float(input("Enter DA: "))
other_allowances = float(input("Enter Other Allowances: "))

gross_salary = basic_salary + hra + da + other_allowances

print("Gross Salary =", gross_salary)
