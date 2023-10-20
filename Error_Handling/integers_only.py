# val=input("Enter number: ")
# if val.isdigit()==False:
#     raise Exception("Only integers allowed")
# else:
#     print("Valid input")


val=input("Enter username: ")
if val.isalnum()==False:
    raise Exception("Only numbers and alphabets are allowed")
else:
    print("Valid input")