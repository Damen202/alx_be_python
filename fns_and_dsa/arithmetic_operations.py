def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation.
    """
    num1 = float(num1)
    num2 = float(num2)
    operation = str(operation)
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'divide':
        if num2 == 0:
            return "number cannot be divided by zero."
        return num1 / num2
    elif operation == 'multiply':
        return num1 * num2
    else:
        return f"Invalid operation: {operation}"
