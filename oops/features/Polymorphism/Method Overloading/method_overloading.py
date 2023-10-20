# Function overloading
# Same function name or method with differnt number of parameters

class Operations:
    def add(self,n1,n2):
        return n1+n2
    def add(self,n1,n2,n3):
        return n1+n2+n3
    def add(self,n1,n2,n3,n4):
        return n1+n2+n3+n4
    
op=Operations()
print(op.add(10,20,30,40))