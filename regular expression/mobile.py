# rule for validating mobile number
from re import*
mob=input("Enter phone number : ")
pattern="(91)?[0-9]{10}"
matcher=fullmatch(pattern,mob)
print("Invalid" if matcher==None else "Valid")