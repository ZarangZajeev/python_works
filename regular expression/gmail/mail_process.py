from re import*
f=open("D:\\MY PC\\july_python_works\\regular expression\\gmail_data.txt")
pattern="[a-z0-9_.]+@[a-z]{2,}.com"

for line in f:
    mail=line.rstrip("\n")
#     print(mail)
    matcher=fullmatch(pattern,mail)
    if matcher!=None:
        print(mail)