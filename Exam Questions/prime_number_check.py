# num=int(input("Enter a number : "))
# is_prime=True
# for i in range(2,num):
#     if(num%i==0):
#         is_prime=False
#         break
# print(is_prime)
# if(is_prime==True):
#     print(f"is not prime number")
# else:
#     print(f"is not prime number")


# num=int(input("Enter a numeber: "))
# is_prime=True
# for i in range(2,num):
#     if(num%i==0):
#         is_prime=False
#         break
# print(is_prime)
# if(is_prime==True):
#     print(f"{num} is prime number")
# else:
#     print(f"{num} is not prime number")

# num=int(input("Enter a number: "))
# is_prime=True
# for i in range(2,num):
#     if(num%i==0):
#         is_prime=False
#         break
# print(is_prime)
# if(is_prime==True):
#     print(f"{num} is prime number")
# else:
#     print(f"{num} is not prime number")

# num=int(input("Enter a number: "))
# is_prime=True
# for i in range(2,num):
#     if(num%i==0):
#         is_prime=False
#         break
# if(is_prime==True):
#     print(f"{num} is prime number")
# else:
#     print(f"{num} is not prime number")


num=int(input("Enter a number: "))
is_prime=True
for i in range(2,num):
    if(num%i==0):
        is_prime=False
        break
if(is_prime==True):
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")