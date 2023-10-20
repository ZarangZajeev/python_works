from re import*
mail=input("Enter Gmail id: ")
# pattern="[a-z0-9_.]+@(gmail|live|).com"
pattern="[a-z0-9_.]+@[a-z]{2,}.com"
matcher=fullmatch(pattern,mail)
print("Invalid mail ID" if matcher==None else "Valid mail ID")