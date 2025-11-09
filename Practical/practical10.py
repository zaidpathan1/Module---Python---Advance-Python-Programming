try:
    # File operation
    file = open("data.txt", "r")
    
    # Division operation
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    
    print(f"Division result: {result}")
    
except FileNotFoundError:
    print("Error: File 'data.txt' not found.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Enter numeric values.")
except Exception as e:
    print(f"Unexpected Error: {e}")
finally:
    try:
        file.close()
    except:
        pass