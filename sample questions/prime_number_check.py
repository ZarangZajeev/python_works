# num=int(input("Enter a number: "))
# is_prime=True

# for i in range(2,num):
#     if(num%i==0):
#         is_prime=False
#         break
# print(is_prime)

# if(is_prime==True):
#     print("is prime number");
# else:
#     print("is not prime number");

num=int(input("Enter a number: "))
is_prime=True
for i in range(2,num):
    if(num%i==0):
        is_prime=False
    break
print(is_prime)
if(is_prime==True):
    print(f"is prime number")
else:
    print("isn't prime number")