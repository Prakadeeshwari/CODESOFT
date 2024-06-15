def calculator():
    print("Welcome to the Simple Calculator!")

    # Prompt the user for input
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter the operation (1/2/3/4): ")

    # Perform the calculation based on the user's choice
    if operation == '1':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation choice. Please enter 1, 2, 3, or 4.")

# Run the calculator
calculator()

# Welcome to the Simple Calculator!
# Enter the first number: 20
# Enter the second number: 60
# Select operation:
# 1. Addition (+)
# 2. Subtraction (-)
# 3. Multiplication (*)
# 4. Division (/)
# Enter the operation (1/2/3/4): 3
# The result of 20 * 60 is: 1200
