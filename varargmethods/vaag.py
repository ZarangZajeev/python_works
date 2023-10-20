# def add(*args): #accept any number of parameters
#     return sum(args)

# print(add(10,20))
# print(add(10,20,30))
# print(add(10,20,30,40))


# def product(*args):
#     res=1
#     for num in args:
#         res=res*num
#     return res

# print(product(10,10))

# def adder(*args):
#     return sum(args)
# print(adder(4,6,4,6))



# def concat(*args):
#     res=""
#     for st in args:
#         res+=st
#     return res
# print(concat("hello","hai"))


# def con(*args):
#     return " ".join(args)
# print(con("SARANG","SAJEEV"))


# def rev_con(*args):
#     data=list(args)
#     data.reverse()
#     return " ".join(data)
# print(rev_con("red","green","blue","white"))



# def person_name(**kwargs):
#     print(kwargs)
# person_name(first_name="Rahul",middle_name="rohit",last_name="ajith")




# def empdetails(**kwargs):
#     # print(kwargs)
#     name=kwargs.get("name")
#     exp=kwargs.get("exp")
#     dep=kwargs.get("dep")
#     print(f"{name} has {exp} year exp in {dep}")
# empdetails(name="Nandhu",exp="4",dep="EY")



def balance_enq(**kwargs):
    bank_name=kwargs.get("bank_name")
    acno=kwargs.get("acno")
    balance=kwargs.get("balance")
    print(f"your {bank_name} {acno} balance is INR {balance}")
    # your sbi 1234 accout bal is INR 245662
balance_enq(bank_name="sbi", acno=12345,balance=155662)


# def perform_operation(*args,**kwargs):
#     num1,num2=args
#     op=kwargs.get("operand")
#     if op=="+":
#         return num1+num2
#     elif op=="-":
#         return num1-num2
#     elif op=="/":
#         return num1/num2
#     elif op=="*":
#         return num1*num2
#     else:
#         return "Invalid input"
# print(perform_operation(10,20,operand="-"))