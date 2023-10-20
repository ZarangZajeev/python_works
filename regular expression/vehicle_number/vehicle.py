from re import*
f=open("D:\\MY PC\\july_python_works\\regular expression\\vehicle_number\\database.txt")
# pattern="[A-Z]{2}[-\s]?\d{2}[-\s]?[A-Z]{1,2}[-\s]?[0-9]{4}"
pattern="(KL)[-\s]?\d{2}[-\s]?[A-Z]{1,2}[-\s]?[0-9]{4}"

for line in f:
    reg_num=line.rstrip("\n")
    # print(reg_num)
    matcher=fullmatch(pattern,reg_num)
    if(matcher!=None):
        print(reg_num)