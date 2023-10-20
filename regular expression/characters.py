from re import*
text="abhjdbjhnctfab DG56466DHD$"
# pattern="[0-9]" /d check for all digits
# pattern="\d"
# pattern="[\D]" #exclude all digits
# pattern="[a-zA-Z0-9]"
# pattern="[^a-z]"    #exclude
# pattern="[^a-zA-z0-9]"
pattern="\w" # all alpha numeric characters
matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())