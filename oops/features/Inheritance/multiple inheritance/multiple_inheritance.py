class P1:
    def m1(slef):
        print("Inside parant 1")
    
class P2:
    # def m2(self):
    def m1(self):                   # Out first object in pyhton
        print("Inside parant 2")

class child(P1,P2):                 # Multiple inheritance
    def m3(self):
        print("Inside child")

ch=child()
ch.m1()
# ch.m2()