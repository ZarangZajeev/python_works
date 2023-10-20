from re import *
text="abtfyghabnababhgh"
patter="ab"
matcher=finditer(patter,text)
for m in matcher:
    print(m.start())
    print(m.group())