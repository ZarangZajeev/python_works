# starting with an alphabet k,l,m,n
# second must be a digit and divisible by 3
# followed by any number of alphabet and digit
from re import*
text=input("Enter text: ")
pattern="[k-n][369][a-zA-Z0-9]*"
matcher=fullmatch(pattern,text)
print("Invalid" if matcher==None else "Valid")