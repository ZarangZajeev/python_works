from re import*
num=input("Enter KL number: ")
pattern="(KL)[-\s]?\d{2}[-\s]?[A-Z]{1,2}[-\s]?\d{4}"
matcher=fullmatch(pattern,num)
print("Invalid number" if matcher==None else "Valid Number")