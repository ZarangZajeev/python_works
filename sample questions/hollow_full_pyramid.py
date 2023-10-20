num=int(input("Enter a number: "))
h=0
for row in range(1, num+1):
    for sp in range(row,num):
        print(" ", end=" ")
    while h!=(2*row-1):
        if(h==0 or h==2*row-2):
            print("*", end=" ")
        else:
            print(" ",end=" ")
        h+=1
    h=0
    print()
for row in range(0,2*num-1):
    print("*", end=" ")

# num = int(input("enter number:"))
# for i in range(1, num):
#     for j in range(0, num-i):
#         print(" ", end = " ")
#     for j in range(0, (i*2)-1):
#         if(i > 0) and i and (j < (i*2)-2):
#             print(" ",end = " ")
#         else:
#             print("*",end =" ")
#     print()