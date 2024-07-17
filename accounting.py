# Task (Accounting)
# Make a dictionary user data with username and password as key and value
# Make another accounting dictionary with username and balance as key and value
# Ask the user for username and password, if the username and password exists print 'login successfull' else 'Invalid credentials' 
# If the login is successfull give user options : 1. View balance 2. Add balance 3. Redeem balance
# If the user says view balance print the balance of user from accounting dictionary
# If the user says add balance ask for how much to add and add it with the balance in accoutning dictionary and print
# If the user says redeem balance ask for much to redeem and reduce it with the balance in accounting dictionary and print

user_data = {'bibash':'don', 'chandra':'chor', 'kaushik':'noob', 'bivek':'chor2'}
accounting = { 'bibash': 10000, 'chandra': 5000, 'kaushik':2000, 'bivek':1000}

username = input("Enter a username: ")
password = input("Enter a password: ")

if username in user_data.keys() and password in user_data.values():
    print("Login Successful")
    while True:
        print("What do you want to check in your account?")
        print("1. View balance")
        print("2. Add balance")
        print("3. Redeem balance")
        choice = input("Enter your option: ")
        
        if choice == '1':
            print("Your balance is: ", accounting[username])
            
        elif choice == '2':
            add_balance = int(input("Enter the amount to add: "))
            accounting[username] += add_balance
            print("Your new balance is: ", accounting[username])
            
        elif choice == '3':
            redeem_balance = int(input("Enter the amount to redeem: "))
            if redeem_balance <= accounting[username]:
                accounting[username] -= redeem_balance
                print("Your new balance is: ", accounting[username])
            
        else:
            print("Invalid option")
            
        
        again_check = input("Do you want to check other option: ")
        if again_check.lower() == 'yes':
            continue
        else:
            print("End of the Program")
            break

else:
    print("Invalid Credentials")