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
        if num2 == '0':
            raise ValueError("number cannot be divided by zero.")
        return num1 / num2
    elif operation == 'multiply':
        return num1 * num2
    else:
        raise ValueError(f"Invalid operation: {operation}")
