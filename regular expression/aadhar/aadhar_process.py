from re import*
f=open("D:\\MY PC\\july_python_works\\regular expression\\aadhar\\aadhar_database.txt")
pattern="\d{4}[\s-]?\d{4}[\s-]?\d{4}"
for line in f:
    aadhar=line.rstrip("\n")
    # print(aadhar)
    matcher=fullmatch(pattern,aadhar)
    if(matcher!=None):
        print(aadhar)