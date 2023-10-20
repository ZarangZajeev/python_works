# text="ABAACCBB"
# character_count={}
# for char in text:
#     if char in character_count:
#         character_count[char]+=1
#     else:
#         character_count[char]=1
# print(character_count)

# text="hello hai hello hai hello"

# text="XHJXNJJDIKDK"
# character_count={}
# for char in text:
#     if char in character_count:
#         character_count[char]+=1
#     else:
#         character_count[char]=1
# print(character_count)

# for k,v in character_count.items():
#     if v==1:
#         print(k)

text="VGJKSFFTJMSHFD"
character_count={}
for char in text:
    if char in character_count:
        character_count[char]+=1
    else:
        character_count[char]=1
print(character_count)
for k,v in character_count.items():
    if(v==1):
        print(k)