from re import*
f=open("D:\\MY PC\\july_python_works\\regular expression\\mobile number\\mobile_data.txt")
pattern="(91)?[-]?[6-9]{1}[0-9]{9}"
for line in f:
    number=line.rstrip("\n")
    # print(number)
    matcher=fullmatch(pattern,number)
    if(matcher!=None):
        print(number)