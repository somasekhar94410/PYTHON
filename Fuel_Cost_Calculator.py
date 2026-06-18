distance = float(input("Enter the distance traveled (in km): "))
mileage = float(input("Enter the vehicle mileage (km per liter): "))
fuel_price = float(input("Enter the fuel price per liter: "))

fuel_consumed = distance / mileage
fuel_cost = fuel_consumed * fuel_price

print("Fuel Consumed =", fuel_consumed, "liters")
print("Total Fuel Cost =", fuel_cost)
