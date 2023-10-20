# validate pyhton variable name
from re import*
var=input("variable name: ")
pattern="[a-zA-Z][a-zA-Z0-9_]*"
matcher=fullmatch(pattern,var)
if matcher==None:
    print("Invalid")
else:
    print("Valid")