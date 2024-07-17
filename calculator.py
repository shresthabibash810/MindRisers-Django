
while True:  
    a = input("Enter a first number: ")

    b = input("Enter a second number: ")

    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        c = input("Enter a operator(+, -, /, *): ")

        def add(a, b):
            return a + b

        def subtract(a, b):
            return a - b

        def multiply(a, b):
            return a * b

        def divide(a, b):
            if b == 0:
                return "Error: Division by zero"
            return a / b

        if  c == '+':
            print('Addition: ', add(a, b))
        elif c == '-':
            print('Subtraction: ', subtract(a, b))
        elif c == '*':
            print('Multiplication: ', multiply(a, b))
        elif c == '/':
            print('Division: ', divide(a, b))
        else:
            print("Inavlid Operator")    

        again = input("Do you want to perform another operation? (yes/no): ").strip().lower()
        if again == 'yes':
            continue
        else:
            break 
          
    else:
        print("Invalid input. Please enter a number only.")
        retry = input("Do you want to try again (yes or no)? ").strip().lower()
        if retry == 'yes':
            continue
        else:
            break
