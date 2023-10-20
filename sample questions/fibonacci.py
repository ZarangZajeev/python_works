num=int(input("Enter the limit: "))
pre=0
cur=1
i=1
print(pre)
print(cur)
while(i<=num):
    next=pre+cur
    print(next)
    pre=cur
    cur=next
    i+=1