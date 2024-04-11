def add_numbers(a, b):
    return a + b

def divide_numbers(a, b):
    return a / b

def divide_numbers_zerodivisionerror(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b


def complex_operations(a, b):
    add_result = a + b
    subtract_result = a - b
    multiply_result = a * b
    divide_result = a / b
    return add_result, subtract_result, multiply_result, divide_result