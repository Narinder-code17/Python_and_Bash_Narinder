# Menu-Driven Calculator
# Python & Bash DevOps Assignment

def addition(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtraction(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiplication(a, b):
    """Return the product of two numbers."""
    return a * b


def division(a, b):
    """Return the division result with zero-division handling."""
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


while True:
    print("\n===== MENU-DRIVEN CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Calculator exited successfully.")
        break

    if choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = addition(num1, num2)

            elif choice == "2":
                result = subtraction(num1, num2)

            elif choice == "3":
                result = multiplication(num1, num2)

            elif choice == "4":
                result = division(num1, num2)

            print("Result:", result)

        except ValueError:
            print("Invalid input. Please enter numbers only.")

    else:
        print("Invalid choice. Please select an option from 1 to 5.")