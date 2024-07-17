# Task (Login program - 2)
# Make a dictionary with user datas, where username are key and password are value
# Ask the user for username and password
# Check the username and pasword in dictionary if it exists print ' Login successfull '
# Else print ' Invalid credentials '

user_data = {'ram': 'ram123', 'hari': 'hari123'}


username = input("Enter your username: ")
password = input("Enter your password: ")


if username in user_data.keys() and  password in user_data.values():
    print("Login successful")
else:
    print("Invalid credentials")