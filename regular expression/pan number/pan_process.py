from re import*
f=open("D:\\MY PC\\july_python_works\\regular expression\\pan number\\pan_data.txt")
pattern="[A-Z]{3}[PCAFHT]{1}[A-Z]{1}\d{4}[A-Z]{1}"
for line in f:
    pan=line.rstrip("\n")
    # print(pan)
    matcher=fullmatch(pattern,pan)
    if(matcher!=None):
        print(pan)