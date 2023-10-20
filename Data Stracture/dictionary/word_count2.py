text="hello, hai hai, hello hello"
words=text.casefold().replace(",","").split(" ")
wc={}
for w in words:
    if w in wc:
        wc[w]=1
    else:
        wc[w]+=1
print(wc)