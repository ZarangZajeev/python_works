lst=[12,25,47,89,56,32,41,25,62]
element=int(input("Enter a element: "))
is_present=False
for i in range(0,len(lst)):
    if(lst[i]==element):
        is_present=True
        break
print(is_present)
print(f"{lst[i]} is present at {i+1}th position")