# temperature conversion 
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
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
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result:.2f}°F")
    elif unit == 'F':
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is {result:.2f}°C")
    else:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()

