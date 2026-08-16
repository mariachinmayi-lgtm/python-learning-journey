unit = input("Enter a unit for temperature, Celsius or Farenheit (C or F):")
temperature = float(input("Enter a temperature"))

if unit == "C":
    temperature = round(((9*temperature)/5)+32,1)
    print(f"The temperature in Farenheit is: {temperature}°F")
elif unit == "F":
    temperature = round(((temperature - 32)*5)/9,1)
    print(f"The temperature in Celsius is: {temperature}°C")
else:
    print(f"{unit} is an invalid unit of measurement")



