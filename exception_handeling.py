# while True:
#     try:
#         a = int(input("Enter a number: "))
#         break
#     except:
#         print("Invalid input")

# print(a)
# # b = 23
# print(a+b) 

try:
    # print(a)
    '23' * '9'
except NameError:
    print("NameError")
except TypeError:
    print("TypeError")
