gender=input("Enter gender ")
tummy=int(input("Enter tummy size: "))
buttock=int(input("Enter buttock size: "))
result=tummy/buttock;
print(f"Value is {result}")
if (gender=="male"):
    if (result<=0.95):
        print("Health rick is Low");
    elif (0.96<= result <= 1.0):
        print("Health rick is Moderate");
    else:
        print("Health rick is High");
elif(gender=="female"):
    if (result<=0.80):
        print("Health rick is Low")
    elif (0.81<= result <= 0.85):
        print("Health rick is Moderate")
    else:
        print("Health rick is High")