def fibonacci(entry):  # Returns the Fibonacci number
    if entry < 2:
        return entry

    a = 1
    b = 0
    result = 0
    while entry >= 0:
        result = a + b
        a = b
        b = result
        entry -= 1

    return result
