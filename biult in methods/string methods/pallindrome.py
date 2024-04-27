s_word="sarang"
count=len(s_word)
p_str=""
for i in range(count-1,-1,-1):
    p_str+=s_word[i]
print(f"Pallindrome" if s_word == p_str else f"Not pallindrome")