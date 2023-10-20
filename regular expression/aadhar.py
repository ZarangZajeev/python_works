from re import*
aadhar=input("Enter number: ")
pattern="\d{4}\s?\d{4}\s?\d{4}"
matcher=fullmatch(pattern,aadhar)
print("Invalid" if matcher==None else "Valid")