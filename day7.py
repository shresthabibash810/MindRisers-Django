# New requirement
# Check whether the user has passed number only in input
# If the user has passed number then do the operation
# But if the user has not passed a number ask for the number again untile the user passes a number
while True:  
    a = input("Enter a first number: ")

    b = input("Enter a second number: ")

    if a.isdigit() and b.isdigit():
        a = int(a)
        b = int(b)
        c = input("Enter a operator(+, -, /, *): ")

        if  c == '+':
            print('Addition: ', a + b)
        elif c == '-':
            print('Subtraction: ', a - b)
        elif c == '*':
            print('Multiplication: ', a * b)
        elif c == '/':
            print('Division: ', a/b)
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

