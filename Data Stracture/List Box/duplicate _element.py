# lst1=[10,13,15,20,25]
# lst2=[12,13,20,25,30]
# lst1.sort()
# lst2.sort()
# lst1_upp=len(lst1)
# lst2_upp=len(lst2)
# for i in range(0,lst1_upp):
#     for j in range(0,lst2_upp):
#         if (lst1[i]==lst2[j]):
#             print(f"Same elements are: {lst1[i]}")
#             break
#         elif(lst1[i]<lst2[j]):
#             i+=1
#             break
#         elif(lst1[i]>lst2[j]):
#             j+=1




lst1=[10,13,15,20,25]
lst2=[12,13,20,25,30]
lst1.sort()
lst2.sort()
p1,p2=0,0
while((p1<len(lst1)) and (p2<len(lst2))):
    if(lst1[p1]==lst2[p2]):
        print(f"Common elements are: {lst1[p1]}")
        p1+=1
        p2+=1
    elif(lst1[p1]<lst2[p2]):
        p1+=1
    elif(lst1[p1]>lst2[p2]):
        p2+=1