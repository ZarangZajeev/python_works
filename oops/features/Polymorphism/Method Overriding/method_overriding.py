class Parent:
    def mobile(self):
        print("One plus Nord CE")

    def car(self):
        print("Polo GT")

class Child(Parent):
    def mobile(self):
        print("IPhone 15 Pro")          # Method Overriding

ch=Child()
ch.mobile()
ch.car()