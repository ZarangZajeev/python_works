from re import*
text="abaabcaabaaaa"
# pattern="a+" # + atleast one a
# pattern="a*" # matches of any number of a
# pattern="a?" # optional eg. (91)?
# pattern="a{2}" #  occarance of a 2
pattern="a{2,3}" # occarance of a miimum 2 maximum 3
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())


# text="The fat tiger run very fast to cath the cat"
# pattern=""
# matcher=finditer(pattern,text)
# for m in matcher:
#     print(m.start(),m.group())