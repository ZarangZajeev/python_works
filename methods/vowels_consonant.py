# word="pneumonoultramicroscopicsilicovolcanoconiosis"
# total=len(word)
# print(f"Total number of characters= {total}")
# vowels="aeiou"
# vowels_cout= sum(word.count(vowel) for vowel in vowels)
# print(f"Number of vowels= {vowels_cout}")
# consonants=total-vowels_cout
# print(f"Number of consonants= {consonants}")

words="pneumonoultramicroscopicsilicovolcanoconiosis"
vowels= 'a','e','i','o','u'
v_count=0
c_count=0
for ch in words:
    if ch in vowels:
        v_count+=1
    elif (ch.isalpha):
        c_count+=1

print(f"Total count ={len(words)} ")
print(f"Total number of vowels= {v_count}")
print(f"Total number of consonants= {c_count}")