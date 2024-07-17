# Logical operator

# And operator - Used between the operations

# a = 23
# b = 34
# c = 54

# d = a < b and b < c

# print(d)

# Or operator - Used between the operations

# a = 23
# b = 34
# c = 54

# d = a > b or b > c

# print(d)

# Not operator - Used in overall operation

# a = 23
# b = 34

# c = not a > b

# print(c)

# Membership operator
# a = 2
# b = [1,2,3,4,'Hello']

# In operator

# c = a in b

# print(c)

# a = 2
# b = [1,2,3,4,'Hello']

# Not in operator

# a = 1
# b = [1,3,4]

# c = a not in b

# print(c)


# Identity operator

# a = 24
# b = 23

# Is operator

# c = a is b

# print(c)

# Is not operator

# c = a is not b

# print(c)

# Conditional statement
a = 23
b = 34

# Requirement
# If A value is greater than B value print 'A is greater'
# But if A value is not greater than B value print 'A is not greater'

# if a > b:
#     print('A is greater')
# elif a == b:
#     print('A is equal to B')
# # elif a < b:
# #     print('A is not greater')
# else:
#     print('Invalid!')

# Input statement

# a = input('Enter a number : ')

# print(a + 23)

# Task
# Requirement
# Make a list of usernames
# Ask the user for his/her username
# If the username exists in the list print 'Login successfull'
# But if the username doesnot exist in the list print 'Invalid credentials'

name = ['Bibash', 'Chandra', 'Kaushik', 'Bivek']
username = input("Enter your username: ")
print(username)

if username in name:
    print("Login Successful")
else:
    print("Invalid Credentials")    


