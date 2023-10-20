# lst=[3,5,4]
# total=sum(lst)
# for i in range(0,len(lst)):
#     res=total-lst[i]
#     print(res)


# lst=[2,4,5,6]
# sum=7 (2,5)
# sum=6 (2,4)
# sum=11 (6,5)



# lst=[2,4,5,6]
# i=0
# j=0
# sum=int(input("Enter the one of the sum values 7,6 or 11: "))
# for i in range(0,3):
#     for j in range(i+1,4):
        
#         if(lst[i]+lst[j]==sum):
#             print(f"Numbers are {lst[i]} and {lst[j]}")
#         elif(lst[i]+lst[j]==sum):
#             print(f"Numbers are {lst[i]} and {lst[j]}")
#         elif(lst[i]+lst[j]==sum):
#             print(f"Numbers are {lst[i]} and {lst[j]}")



sum=int(input("Enter sum (6,8,9,10,11,12,13,14,15,): "))
arr=[2,4,6,7,8]
# srt_arr=sorted(arr)
arr.sort()
low=0
upp=len(arr)-1
while(low<upp):
    cur_sum=arr[low]+arr[upp]
    if(cur_sum==sum):
        print(f"Paits are: {arr[low]} and {arr[upp]}")
        # break
        low+=1
        upp-=1
    elif(cur_sum<sum):
        low+=1
    elif(cur_sum>sum):
        upp-=1