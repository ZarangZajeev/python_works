# num1=int(input("Enter the lower number: "))
# num2=int(input("Enter the higher number: "))
# largest_number=0
# for i in range(2,num1+1):
#     if(num1%i==0):
#         print(i)




#         for high in range(2,i):
#             if high>largest_number:
#                 largest_number=high
# print(f"HCF of {num1} and {num2} is= {largest_number}")


# low=int(input("Enter the lower element: "))
# up=int(input("Enter the upper element: "))
# temp=int(0)
# reminder=up/low;
# for i in range(2,low+1):
#     if (reminder!=0):
#         temp=up
#         up=low
#         low=reminder
# print(reminder)



num1=int(input("Enter the lower number: "))
num2=int(input("Enter the higher number: "))
max_hcf= num1 if num1<num2 else num2
for i in range(max_hcf, 0,-1):
    if (num1%i==0 and num2%i==0):
        if(i>max_hcf):
            max_hcf=i
        # print(i)
if(max_hcf>1):
    print(f"The largest HCF is: {max_hcf}")
elif(max_hcf==1):
    print("No commomn factor")