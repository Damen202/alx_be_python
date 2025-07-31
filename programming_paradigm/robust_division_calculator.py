# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        return f"Result: {result:.2f}"
    except ValueError:
        return "Error: Cannot divide by zero"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"