word="goodmorning"
count=len(word)
# for i in range(0,count):
#     print(word[i])
srt=sorted(word)
print(srt)
for i in range(0,count-1):
    j=i+1
    if (srt[i]==srt[j]):
        print(f"Duplicate charater- {srt[i]}")