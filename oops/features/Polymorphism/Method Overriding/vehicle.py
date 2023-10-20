class Parent:
    def vehicles(self):
        self.context=["Passion Pro","Swift"]
        return self.context
    
class Child(Parent):
    def vehicles(self):
        self.context=super().vehicles()         # super() pointing to parent objects
        self.context.append("Ola")              # self pointing to current object
        return self.context
    
p=Parent()
print(p.vehicles())

ch=Child()
print(ch.vehicles())