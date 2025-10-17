import os
os.system('cls')

choice = input("Välj en omvandling:\n A = Celsius till Fahrenheit & Kelvin\n B = Fahrenheit till Celsius & Kelvin\n C = Kelvin till Celsius & Fahrenheit\n D = Avsluta programmet\n")

if input == "A":
    def celsius_to_fahrenheit():
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    def fahrenheit_to_celsius():
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius}°C")


def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius}°C")

def kelvin_to_celsius():
    kelvin = float(input("Enter temperature in Kelvin: "))
    celsius = kelvin - 273.15
    print(f"{kelvin}K is equal to {celsius}°C")


celsius_to_fahrenheit()
fahrenheit_to_celsius()
kelvin_to_celsius()