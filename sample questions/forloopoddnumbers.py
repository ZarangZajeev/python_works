low=int(input("Enter the lower limit: "))
up=int(input("Enter the upper limit: "))
for num in range(low,up+1):
    if(num%2!=0):
        print(num);