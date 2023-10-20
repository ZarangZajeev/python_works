text="TGHSKTHSDGHSH"
wc={}
for ch in text:
    if ch in wc:
        print(f"{ch} is first repeated character")
        break
    else:
        wc[ch]=1