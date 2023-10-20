num=int(input("Enter a number: "))
for row in range(1,num+1):
    for space in range(num-1,row-1,-1):
        print(end=" ")
    for star in range(1, row+1):
        print("* ",end=" ")
    print()