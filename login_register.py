#Requirements
#Ask the user: Login or Register
#If Login, ask for username and password 
#If Register, ask for username, password, and confirm password

import json 
user_choice = input("Do you want to login or register : ").lower()

def login():
    username = input("Enter your username : ")
    password = input("Enter your password : ")

    f = open('user_data.txt', 'r')
    user_data =f.read()
    f.close()
    # print(user_data)
    
    list_user_data = user_data.split('-')
    # print(list_user_data)
    user_login = False

    for i in list_user_data:
        if i != '':
            dict_data = json.loads(i)
            if username in dict_data and password == dict_data[username]:
                user_login = True

    if user_login == True:
        print("Login Successful")
    else:
        print("Invalid username or password")

def register():
    username = input("Enter your username : ")
    password = input("Enter your password : ")

    user_data = {username:password}

    json_data = json.dumps(user_data)
    
    f = open('user_data.txt', 'a')
    f.write(json_data+'-')
    f.close()
    

if user_choice == 'login':
    login()
elif user_choice == 'register':
    register()