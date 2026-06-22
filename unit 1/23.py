annual_income = float(input("Enter Annual Income: "))
tax_rate = float(input("Enter Tax Rate (%): "))

tax_amount = (annual_income * tax_rate) / 100
net_income = annual_income - tax_amount

print("Income Tax =", tax_amount)
print("Net Income After Tax =", net_income)