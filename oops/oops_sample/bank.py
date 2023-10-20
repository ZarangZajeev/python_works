class Bank:
    acc_no:int
    acc_type:str
    balance:int
    bank_name:str="Central Bank"
    amount:int

    # def create_account(self,accno,acctype,bal,bankname):
    #     self.acc_no=accno
    #     self.acc_type=acctype
    #     self.balance=bal
    #     self.bank_name=bankname

    def __init__(self,accno,acctype,bal):   # constructor initialise objects
        self.acc_no=accno
        self.acc_type=acctype
        self.balance=bal


    # def __init__(self,accno,acctype,bal):
    #     self.acc_no=accno
    #     self.acc_type=acctype
    #     self.balance=bal
    #     self.bank_name="SBI"

    def display(self):
        print(f"account number {self.acc_no} with {self.acc_type} has balance {self.balance} in {Bank.bank_name}")

    def withdrawal(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance=self.balance-amount
            print(f"Withdrew {amount} | New balance: {self.balance}")
        else:
            print("Cannot process withdrawal")

    def deposite(self,amout):
        if(amout>0):
            self.balance+=amout
            print(f"Deposited amount= {amout} | New balance= {self.balance}")
        else:
            print("Cannot process deposite")

    def balance_enq(self):
        print(f"Your account balance is {self.balance}")


acc_holder1=Bank(3400001085,"Savings",1500)
# acc_holder1=Bank(3400001085,"Savings",1500)
# acc_holder1.display()
# acc_holder1.withdrawal(500)
# acc_holder1.deposite(200)
# acc_holder1.balance_enq()


acc_holder2=Bank(10002354,"Current Account",2500)
# acc_holder2=Bank(10002354,"Current Account",2500)
# acc_holder2.create_account(10002354,"Current Account",2500,"Canera Bank")
# acc_holder2.withdrawal(1000)
acc_holder2.deposite(500)
acc_holder2.display()
acc_holder2.withdrawal(200)
