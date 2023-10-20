num=int(input("Enter a number "))
for row in range(num,0,-1):
    for col in range(0, row):
        print("*", end="    ")
    print()