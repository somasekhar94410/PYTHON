import math

number = float(input("Enter a number: "))
power_value = float(input("Enter the power value: "))

print("Square Root =", math.sqrt(number))
print("Power =", math.pow(number, power_value))
print("Sine =", math.sin(math.radians(number)))
print("Cosine =", math.cos(math.radians(number)))
print("Tangent =", math.tan(math.radians(number)))