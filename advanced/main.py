from operations import add, divide, multiply, subtract
from utils import get_operation, get_user_number

number_1 = get_user_number("Enter the first number: ")
operation = get_operation()
number_2 = get_user_number("Enter the second number: ")

def main():
    if operation == "/":
        while number_2 == 0:
            print("Error: Cannot divide by zero.")
            num_2 = get_user_number("Enter a new second number: ")

if operation == "+":
        result = add(number_1, number_2)
elif operation == "-":
        result = subtract(number_1, number_2)
elif operation == "*":
        result = multiply(number_1, number_2)
elif operation == "/":
        result = divide(number_1, number_2)

print(f"Result: {number_1} {operation} {number_2} = {result}")

if __name__ == "__main__":
    main()