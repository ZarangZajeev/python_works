op=open("D:\\MY PC\\july_python_works\\file operation\\news.txt",)
wc={}
for line in op:
    words=line.rstrip("\n").split()
    for w in words:
        if w not in wc:
            wc[w]=1
        else:
            wc[w]+=1
print(wc)