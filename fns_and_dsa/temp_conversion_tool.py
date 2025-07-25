FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 5/9
# temperature conversion
def CELSIUS_TO_FAHRENHEIT_FACTOR(celsius):
    return (celsius * 9/5) + 32

def FAHRENHEIT_TO_CELSIUS_FACTOR(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Main logic
def main():
    print("=== temperature conversion ===")
    print(f"FAHRENHEIT_TO_CELSIUS_FACTOR: {FAHRENHEIT_TO_CELSIUS_FACTOR}")
    print(f"CELSIUS_TO_FAHRENHEIT_FACTOR: {CELSIUS_TO_FAHRENHEIT_FACTOR}")
    temp_input = input("Enter the temperature to convert: ")
    unit = input("Is this in Celsius or Fahrenheit? (C/F): ")

    try:
        temperature = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
    
    if unit == 'C':
        result = FAHRENHEIT_TO_CELSIUS_FACTOR(temperature)
        print(f"{temperature}°C is {result:.2f}°F")
    elif unit == 'F':
        result = CELSIUS_TO_FAHRENHEIT_FACTOR(temperature)
        print(f"{temperature}°F is {result:.2f}°C")
    else:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()

