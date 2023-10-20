age=int(input("Eneter a age: "))
if(age<18):
    raise Exception("Invalid age")
else:
    print("Valid age")