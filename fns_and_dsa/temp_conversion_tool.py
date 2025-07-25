# temperature conversion 8
FAHRENHEIT_TO_CELSIUS_FACTOR and CELSIUS_TO_FAHRENHEIT_FACTOR to store the conversion factors
def CELSIUS_TO_FAHRENHEIT_FACTOR(celsius):
    return (celsius * 9/5) + 32

def FAHRENHEIT_TO_CELSIUS_FACTOR(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Main logic
def main():
    print("=== temperature conversion ===")

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

