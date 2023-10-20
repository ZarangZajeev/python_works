from re import*
pan=input("Ente pan number: ")
pattern="[A-Z]{3}[PCAFHT]{1}[A-Z]{1}\d{4}[A-Z]{1}"
matcher=fullmatch(pattern,pan)
print("Invalid" if matcher==None else "Valid")