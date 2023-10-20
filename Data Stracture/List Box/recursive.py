text="ABCDCEFE"
lst=[]
dup_lst=[]
for ch in text:
    char_count=lst.count(ch)
    if char_count==0:
        lst.append(ch)
    else:
        dup_lst.append(ch)
        # print(f"{ch} is the first recursive character")
        # break
print(f"Second recursice character is= {dup_lst[-1]}")