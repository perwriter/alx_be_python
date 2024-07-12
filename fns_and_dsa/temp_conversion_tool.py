FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temp = float(input("Enter the temperature to convert:"))
    choice = input("Is this temperature in Celsius or Fahrenheit? (C/F):").lower()
    if choice == 'f':
       converted_celsius =  convert_to_celsius(temp)
       print(f"{temp}F is {converted_celsius}C")
    elif choice == 'c':
        converted_fahrenheit = convert_to_fahrenheit(temp)
        print(f"{temp}C is {converted_fahrenheit}")
    else:
        print("Invalid temperature. Please enter a numeric value.")
main()