source_word="CHICKEN"
target_word="CICK"
source_list=[]
target_list=[]
is_kangaroo=False
for ch in source_word:
    source_list.append(ch)
for cha in target_word:
    target_list.append(cha)
for cha in target_list:

    ch_count=source_list.count(cha)         # way 1
    if(ch_count>0):
        source_list.remove(cha)
        is_kangaroo=True

    # if cha in source_list:              # another way 
    #     source_list.remove(cha)
    #     is_kangaroo=True

    else:
        is_kangaroo=False
        break

print(is_kangaroo)
if(is_kangaroo==True):
    print(f"This is Kangaroo word")
else:
    print(f"This is not Kangaroo word")