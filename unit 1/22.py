principal = float(input("Enter Loan Amount: "))
annual_rate = float(input("Enter Annual Interest Rate (%): "))
months = int(input("Enter Loan Tenure (Months): "))

monthly_rate = annual_rate / (12 * 100)

emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / \
      ((1 + monthly_rate) ** months - 1)

print("Monthly EMI =", round(emi, 2))