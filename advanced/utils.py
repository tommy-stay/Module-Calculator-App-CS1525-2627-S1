def get_user_number(prompt_message: str) -> float:
    """Asks the user for a number, validates the input, and returns a valid float."""
    while True:
        user_input = input(prompt_message)

        if user_input.replace(".", "", 1).isdigit() or (
                user_input.startswith("-") and user_input[1:].replace(".", "", 1).isdigit()):
            return float(user_input)
        else:
            print("Not allowed. Please enter a valid number.")


def get_operation() -> str:
    """Asks the user for an operation symbol, validates it, and returns the symbol."""
    valid_symbols = ["+", "-", "*", "/"]
    while True:
        sign = input("Enter a sign (+, -, *, /): ").strip()
        if sign in valid_symbols:
            return sign
        print("Can't choose that. Please choose from +, -, *, /.")