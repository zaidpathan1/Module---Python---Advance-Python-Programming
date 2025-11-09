try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    operation = input("Enter operation (+, -, *, /): ")
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        raise ValueError("Invalid operation")
    
    print(f"Result: {result}")

except ZeroDivisionError:
    print("❌ Error: Division by zero is not allowed.")
except ValueError as ve:
    print(f"❌ Error: {ve}")
except Exception as e:
    print(f"❌ Unexpected Error: {e}")