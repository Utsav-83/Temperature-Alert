# Temperature Check Program

# Input temperature in Celsius
temp = float(input("Enter temperature in Celsius: "))

# Conditions
if temp < 20:
    print("It's Cold ❄")
elif 20 <= temp <= 30:
    print("It's Normal 🙂")
else:
    print("It's Hot 🔥")