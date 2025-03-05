def display_menu():
    print("***Welcome to the basic calculator program by Ashley***")
    print("Program to perform basic operations of Add, Subtract, Multiply, Divide, and Remainder")
    print("\nMenu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Remainder")
    print("6. Exit")

def get_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def perform_operation(choice, num1, num2):
    if choice == 1:
        return num1 + num2
    elif choice == 2:
        return num1 - num2
    elif choice == 3:
        return num1 * num2
    elif choice == 4:
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    elif choice == 5:
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 % num2

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Select an operation (1-6): "))
            if choice == 6:
                print("Exiting the program. Goodbye!")
                break
            elif choice in [1, 2, 3, 4, 5]:
                num1, num2 = get_numbers()
                result = perform_operation(choice, num1, num2)
                print(f"Result: {result}")
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
