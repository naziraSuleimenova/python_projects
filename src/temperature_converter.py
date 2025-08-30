
temperature_scale = input("Convert to (F/C): ").upper()

if temperature_scale == "F":
    celsius = int(input("Enter temperature in Celsius: "))
    fahrenheit = int(celsius * 9 / 5 + 32)
    print(str(celsius) + "°C = " + str(fahrenheit) + "°F")

elif temperature_scale == "C":
    fahrenheit = int(input("Enter temperature in Fahrenheit: "))
    celsius = int((fahrenheit - 32) * 5 / 9)
    print(str(fahrenheit) + "°F = " + str(celsius) + "°C")

else:
    print("Please enter 'F' or 'C'.")

