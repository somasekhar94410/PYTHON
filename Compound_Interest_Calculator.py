principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (%): "))
time = float(input("Enter the time period (years): "))

amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

print("Amount =", amount)
print("Compound Interest =", compound_interest)
