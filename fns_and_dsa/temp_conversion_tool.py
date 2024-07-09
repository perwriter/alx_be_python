# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Write a function convert_to_celsius(fahrenheit) 
# that takes a temperature in Fahrenheit and returns the temperature converted to Celsius.
def convert_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit: Temperature in Fahrenheit (float).

    Returns:
        Temperature in Celsius (float).
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Write a function convert_to_fahrenheit(celsius) 
# that takes a temperature in Celsius and returns the temperature converted to Fahrenheit.
def convert_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit.

    Args:
        celsius: Temperature in Celsius (float).

    Returns:
        Temperature in Fahrenheit (float).
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    """Prompts user for temperature conversion and displays the result."""

    while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

            if unit == "C":
                converted_temp = convert_to_fahrenheit(temperature)
                unit = "F"
            elif unit == "F":
                converted_temp = convert_to_celsius(temperature)
                unit = "C"
            else:
                raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

            print(f"{temperature:.1f}°{unit} is {converted_temp:.1f}°C")
            break

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
