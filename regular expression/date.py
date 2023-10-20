from re import*
date=input("Enter date: ")
pattern="\d{4}[-]\d{2}[-]\d{2}"
matcher=fullmatch(pattern,date)
print("Invalid date" if matcher==None else "Valid date")