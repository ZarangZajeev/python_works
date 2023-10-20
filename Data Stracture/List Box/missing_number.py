# lst=[1,2,3,4,6]
# # max_num=max(lst)
# max_num=lst[-1]
# total=max_num*(max_num+1)//2
# cur_num=sum(lst)
# diff=total-cur_num
# print(f"Missing number is {diff}")
# if(diff==0):
#     print(max_num+1," is missing")


lst=[1,2,3,4,6]
# max_num=max(lst)
max_num=lst[-1]
i=0
while(i<max_num):
    j=i+1
    diff=lst[j]-lst[i]
    if(diff==1):
        i+=1
    else:
        print(lst[i]+1," is missing")
        break

# lst1[10,13,15,20,25]
# lst2[12,13,20,25,30]