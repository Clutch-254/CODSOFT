def calculator():
    
    # prompts user for first number from user with error handling
    while True:
        try:
            num1 = float(input("Enter first number: "))
            break
        #if anything other than an integer or float is selected by user then the error message appears in terminal
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Get second number from user with error handling
    while True:
        try:
            num2 = float(input("Enter second number: "))
            break
         #if anything other than an integer or float is selected by user then the error message appears in terminal
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # display operation choices, i gave them numbers for uniqueness as per assignment instructions
    print("\nOperation choices:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    # promps user for operation 
    while True:
        choice = input("\nEnter operation choice (1-4): ")
        if choice in ['1', '2', '3', '4']:
            break
        # if a number other than 1, 2, 3 or 4 is fed then the error message will appear
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
    
    # Performs calculation based on user's choice
    if choice == '1':
        result = num1 + num2
        operation = '+'
    elif choice == '2':
        result = num1 - num2
        operation = '-'
    elif choice == '3':
        result = num1 * num2
        operation = '*'
    elif choice == '4':
        # Handle division by zero
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
        operation = '/'
    
    # Display the result
    print(f"\nResult: {num1} {operation} {num2} = {result}")

# Run the calculator
if __name__ == "__main__":
    calculator()