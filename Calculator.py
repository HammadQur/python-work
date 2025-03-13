# Function to add two numbers
def add(  a, y):
    return int(a + y)

# Function to subtract two numbers
def subtract(a, y):
    return int(a - y)

# Function to multiply two numbers
def multiply(a, y):
    return int(a * y)

# Function to divide two numbers
def divide(a, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return int(a / y)

# Main program
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Take user input
    choice = input("Enter choice (1/2/3/4): ")

    # Take input for the numbers
    num1 = float(input("Enter first Digit: "))
    num2 = float(input("Enter second Digit: "))

    # Perform calculation based on user's choice
    if choice == '1':
        print(f"{int(num1)} + {int(num2)} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{int(num1)} - {int(num2)} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{int(num1)} * {int(num2)} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{int(num1)} / {int(num2)} = {divide(num1, num2)}")
    else:
        print("Invalid Input")

# Call the calculator function
calculator()

