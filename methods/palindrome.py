s_word=("hello")
count=len(s_word)
p_str=""
for i in range(count-1,-1,-1):
    p_str+s_word[i]
# print(p_str)
print("Palindrome" if s_word==p_str else "Not Pallindrome")