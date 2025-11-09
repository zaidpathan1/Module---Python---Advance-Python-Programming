class NegativeNumberError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    print(f"You entered: {num}")
except NegativeNumberError as ne:
    print(ne)
except ValueError:
    print("Invalid input. Please enter an integer.")