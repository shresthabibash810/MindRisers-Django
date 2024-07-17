# # Requirement
# # Ask the user for login or register
# # If the user says register, ask for username and password and make it a relational user data and write it on a file
# # If the user says login, ask for username and password and check it in the file whether the user data exists or not
#     # If the login successfull, give user choices: 1.  add product 2. view product
#     # If the user enter Add product choice, ask for product name, description, price , make these value a relational product data and write it on a file
#     # If the user says view product, read the file where products are stored and print all the products


#During Login, if the user is buyer give him/her choices: 1.View product 2. View Bills
#View Product, Print all the products added by seller
#Then ask for a product does he/she wants to purchase
#Ask for the quantity of purchase
# make a bill data, buyer name, product name, quantity, total write this data on a file

# 2. View bills, print all the buyer bills
import json 

user_choice = input("Do you want to login or register : ").lower()

def login():
    username = input("Enter your username : ")
    password = input("Enter your password : ")

    with open('user_data.txt', 'r') as f:
        user_data = f.read()

    list_user_data = user_data.split('\n')
    user_login = False
    user_type = ''

    for i in list_user_data:
        if i != '':
            dict_data = json.loads(i) #Convert JSON string to dict
            if username == dict_data.get('username') and password == dict_data.get('password'):
                user_login = True
                user_type = dict_data.get('user_type')
                break

    if user_login:
        print("Login Successful")
        if user_type.lower() == 'seller':
            while True:
                print("1. Add product")
                print("2. View product")
                print("3. LogOut")

                choice = input("What do you want to choose: ")
                if choice.lower() == '1':
                    addproduct(username)

                elif choice.lower() == '2':
                    viewproduct()

                elif choice.lower() == '3':
                    print("You are logged out")
                    break
                else:
                    print("Invalid choice")
                    break
        elif user_type.lower() == 'buyer':
            while True:
                print("1. View products")
                print("2. View bills")
                print("3. LogOut")

                choice = input("What do you want to choose: ")
                if choice.lower() == '1':
                    view_product_buyer(username)
                elif choice.lower() == '2':
                    view_bill(username)
                elif choice.lower() == '3':
                    print("You are logged out")
                    break
                else:
                    print("Invalid choice")
                    break                             
    else:
        print("Invalid username or password")

def register():
    username = input("Enter your username : ")
    password = input("Enter your password : ")
    user_type = input("Enter your type (Seller/Buyer): ")

    user_data = {'username': username,
                 'password': password,
                 'user_type': user_type
                 }

    json_data = json.dumps(user_data) #Convert dict into JSON string
    
    with open('user_data.txt', 'a') as f:
        f.write(json_data + '\n')
    
    print("Registration Successful")

def addproduct(seller_name):
    product_name = input("Enter product name : ")
    product_description = input("Enter product description : ")
    product_price = input("Enter product price : ")
    
    product_data = {'Seller': seller_name,
                    'Product': product_name, 
                    'Description': product_description, 
                    'Price': product_price}
    
    json_product_data = json.dumps(product_data)
    
    with open('product_data.txt', 'a') as f:
        f.write(json_product_data + '\n')
    
    print("Product Added Successfully")

def viewproduct():
    with open('product_data.txt', 'r') as f:
        product_data = f.read()

    list_product_data = product_data.split('\n')
    for i in list_product_data:
        if i != '':
            dict_product = json.loads(i)
            print(dict_product)

def view_product_buyer(buyer_name):
    viewproduct()
    product_name = input("Enter a product you want to purchase: ")
    quantity = int(input("Enter the quantity: "))
    with open('product_data.txt', 'r') as f:
        product_data = f.read()
    list_product_data = product_data.split('\n')
    product_found = False
    
    for i in list_product_data:
        if i != '':
            dict_product = json.loads(i)
            if dict_product.get('Product') == product_name:
                product_found = True
                break

    if product_found:
        product_price = dict_product.get('Price')
        total = float(quantity) * float(product_price)
        bill_data = {'Buyer': buyer_name,
                     'Product': product_name,
                     'Quantity': quantity,
                     'Total': total}
        
        json_bill_data = json.dumps(bill_data)

        with open('bill.txt', 'a') as f:
            f.write(json_bill_data + '\n')

        print("Purchase Successful. Bill Created") 
    else:
        print("Product not found")


def view_bill(buyer_name):
    with open('bill.txt', 'r') as f:
        bill_data = f.read()

    list_bill_data = bill_data.split('\n')
    for i in list_bill_data:
        if i != '':
            dict_bill_data = json.loads(i)
            if dict_bill_data.get('Buyer') == buyer_name:
                print("Product: ", dict_bill_data.get('Product'))
                print("Quantity: ", dict_bill_data.get('Quantity'))
                print("Total: ", dict_bill_data.get('Total'))

if user_choice == 'login':
    login()
elif user_choice == 'register':
    register()
else:
    print("Thank You")
