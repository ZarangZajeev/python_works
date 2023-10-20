# try                   :Block           : Doubtfull codes
# except                :Block           : Handling code when try occured
# finally               :Block           : Mandartry message
# raise                 :Keyword         : Custome Message



n1=int(input("Enetr a number 1: "))
n2=int(input("Enter a number 2: "))
lst=[24,46,76]
pos=int(input("Enetr a posiotion: "))

try:
    print(lst[pos])
except Exception as e:
    print(e.args)

try:
    res=n1/n2
    print(f"Result= {res}")
except Exception as e:
    print(e.args)


finally:
    print("Database commit")
    print("File transaction")