# current date and time
from datetime import datetime, timedelta

def display_current_datetime():
    now = datetime.now()
    print("Current date and time:", now)
    print("Formatted date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

# Part 2: Calculate a Future Date
def calculate_future_date(days_ahead):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_ahead)
    print("Future Date after", days_ahead, "day(s):", future_date.strftime("%Y-%m-%d"))

# Main logic
def main():
    print("=== Date and Time Utility ===")
    
    # Part 1: Display current date and time
    display_current_datetime()
    
    # Part 2: Ask user for number of days to add
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")

if __name__ == "__main__":
    main()