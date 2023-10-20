num=int(input("Enter a number: "))
lst=[num%i==0 for i in range(2,num)]
print("Prime" if any(lst)==False else "Not Prime")