num=int(input("Enter a number: "))
for row in range(1,num+1):
    for col in range(0,row):
        print("*",end="    ")
    print()