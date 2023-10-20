lst=[5,7,98,14,67,98,34]
num=int(input("Enter a number: "))
for i in range(0,len(lst)):
    if (num==lst[i]):
        print(f"Element found at position {i+1}")
        break
else:
    print("Element not found")