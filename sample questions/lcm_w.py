# num1=int(input("Enter two numbers: "))
# num2=int(input())
# max=num1 if num1<num2 else num2
# for i in range(1,max+1):
#      if (num1%i==0 and num2%i==0):
#           hcf=i

# lcm=(num1*num2)//hcf

# print(f"LCM is : {lcm}")


num1=int(input("Enter two numbers: "))
num2=int(input())
lcm=0
product=int(num1*num2)
lg_num=num1 if num1>num2 else num2
for i in range(lg_num, product+1):
     if(i%num1==0 and i%num2==0):
        lcm=i
        break
print(lcm)