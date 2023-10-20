from re import*
f=open("D:\\MY PC\\july_python_works\\regular expression\\date\\text_date.txt")
# pattern="(20)\d{2}[-]\d{2}[-]\d{2}"
# pattern="(20)([01][0-9]|2[0-3])[-]\d{2}[-]\d{2}"
# pattern="(20)([01][0-9]|2[0-3])[-](0[1-9]|1[0-2])[-]([0-2][1-9]|3[01])"
pattern="(20)([01][0-9]|2[0-3])[-](0[1-9]|1[0-2])[-]([0][1-9]|[12][0-9]|3[01])"

for line in f:
    date=line.rstrip("\n")
    # print(date)
    matcher=fullmatch(pattern,date)
    if(matcher!=None):
        print(date)