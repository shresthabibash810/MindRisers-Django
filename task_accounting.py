# Accounting program
# Ask user for login or register
# After the login successfull give him/her choices : 1. view balance 2. add balance 3. redeem balance
# 1. View balance : print the balance of the user by reading the file where balance is stored
# 2. Add balance : read the file where balance is stored and find whether the user has balance or not if there is then add in existing balance if not create a new one
# 3. redeem balance : read the file where balance is stored and find whether the user has balance or not if there is then deduct in existing balance if not print 'you do not have balance'
import json
choice = input("Do you want to login or register? ")

def register():
    print("----------------------------------")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    print("----------------------------------")

    account_data = {"username":username,
                    "password": password,
                    "balance": 0}
    json_data = json.dumps(account_data)

    file = open("account.txt", "a")
    file.write(json_data+'-')
    file.close()
    print("Account created successfully")

def login():
    print("----------------------------------")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    print("----------------------------------")
    file = open("account.txt", "r")
    data = file.read()
    file.close()
    data = data.split('-')
   
    user_login = False
    for i in data:
        if i != '':
            dict_data = json.loads(i)
            if username == dict_data.get('username') and password == dict_data.get('password'):
                user_login = True
                break
    

    

    if user_login:
        print("Login successful")
        while True:
            print("----------------------------------")
            print("1. View balance \n2. Add balance \n3. Redeem balance \n4.Log Out")
            print("----------------------------------")
            choice = int(input("Enter your choice: "))
            print("----------------------------------")
            if choice == 1:
                view_balance()
            elif choice == 2:
                add_balance()
            elif choice == 3:
                redeem_balance()
            elif choice == 4:
                print("Logging out")
                break
            else:
                print("Invalid choice")
                break
            

    else:
        print("Login failed")


def view_balance():
    file = open("account.txt", "r")
    data = file.read()
    file.close()
    data = data.split('-')
    print(data)
    for i in data:
        if i != '':
            dict_data = json.loads(i)
            
            print("Your balance is: ", dict_data.get('balance'))


def add_balance():
    file = open("account.txt", "r")
    data = file.read()
    file.close()
    data = data.split('-')
    

    for i in data:
        if i != '':
            dict_data = json.loads(i)

            print("Your balance is: ", dict_data["balance"])
            print("Enter the amount you want to add: ")
            amount = int(input("Enter the amount: "))
            dict_data["balance"] += amount
            print("Your new balance is: ", dict_data["balance"])
            file = open("account.txt", "w")
            file.write(json.dumps(dict_data))
            file.close()
            

def redeem_balance():
    file = open("account.txt", "r")
    data = file.read()
    file.close()
    data = data.split('-')
    for i in data:
        if i != '':
            dict_data = json.loads(i)
            print("Your balance is: ", dict_data["balance"])
            print("Enter the amount you want to reedem: ")
            amount = int(input("Enter the amount: "))
            dict_data["balance"] -= amount
            print("Your new balance is: ", dict_data["balance"])
            file = open("account.txt", "w")
            file.write(json.dumps(dict_data))
            file.close()

    
if choice == 'login':
    login()
elif choice == 'register':
    register()
else:
    print("Invalid choice")
    