try:
    # Code that may raise an exception
    result = 10 / 2  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Code to handle the specific exception
    print("Error: Cannot divide by zero")
else:
    # Code to execute if no exception occurred in the try block
    print("Division successful:", result)
finally:
    # Cleanup code that will be executed regardless of exceptions
    print("Cleanup code: Closing resources")