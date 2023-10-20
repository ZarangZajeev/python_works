lst=[23,45,67,89,24,78,12,24,32,10]
element=int(input("Enter the element to be search: "))
lst.sort()
low=0
upp=len(lst)-1
is_present=False
while(low<=upp):
    mid=(low+upp)//2
    if(element==lst[mid]):
        is_present=True
        break
    elif(element<lst[mid]):
        upp=mid-1
    elif(element>lst[mid]):
        low=mid+1
print(is_present)
if(is_present==True):
    print(f"The element {element} is present")