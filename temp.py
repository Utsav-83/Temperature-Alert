# Temperature Check Program with Celsius to Fahrenheit Conversion

# Input temperature in Celsius
temp_celsius = float(input("Enter temperature in Celsius: "))

# Conversion formula: F = (C × 9/5) + 32
temp_fahrenheit = (temp_celsius * 9/5) + 32

# Conditions for Celsius
if temp_celsius < 20:
    condition = "Cold ❄"
elif 20 <= temp_celsius <= 30:
    condition = "Normal 🙂"
else:
    condition = "Hot 🔥"

# Output
print(f"\nTemperature in Celsius: {temp_celsius}°C")
print(f"Temperature in Fahrenheit: {temp_fahrenheit}°F")
print("Condition:", condition)