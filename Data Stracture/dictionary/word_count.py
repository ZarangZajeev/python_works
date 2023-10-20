text="hello hai hello hai hello"
words=text.split()
print(words)
word_count={}
for word in words:
    word=word.lower()
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
print(word_count)
max_count=max(word_count,key=word_count.get)
print(f"The most common word is {max_count}")