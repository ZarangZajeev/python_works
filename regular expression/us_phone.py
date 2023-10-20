from re import*
mob=input("Enter number: ")
pattern="\d{3}[-\s]?\d{3}[-\s]?\d{4}"
matcher=fullmatch(pattern,mob)
print("Invalid" if matcher==None else "Valid")