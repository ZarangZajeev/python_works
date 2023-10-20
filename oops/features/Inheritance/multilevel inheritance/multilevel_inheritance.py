class P1:
    def m1(self):
        print("From parent 1")
class P2(P1):
    def m2(self):
        print("From parent 2 and its from parent 1")
class child(P2):
    def c(self):
        print("From child and its from parent 1 and 2")

ch=child()
ch.c()
ch.m1()