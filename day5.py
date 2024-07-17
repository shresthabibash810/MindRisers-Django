#Loop
# The state doing something constantly, again and again
# Running a statement agai and again

# While Loop, For Loop

#While Lopp - Conditional Loop

# a = 5
# b = 0
# c = 2

# while a>b:
#     print("Hello world")
#     b += 1
#     if b == 5:
#         print('Loop will end')
#     while c > b:
#         print('C is greater')    
#         b += 1

# keywords in loop

# count = 0
# while True:
#     print('Hello World')
#     count += 1
#     if count == 2:
#         continue
#     if count == 5:
#         break
#     print('Loop')

# statement = input("Enter your statement: ")
# user_time = int(input("how much Time you want to loop: "))
# count = 0
# while user_time > count:
#     print(statement)
#     count+=1

# while True:
#     print(statement)
#     count += 1
#     if count == user_time:
#         break

while True:  
    a = int(input("Enter a first number: "))

    b = int(input("Enter a second number: "))

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
    