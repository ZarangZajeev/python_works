class Super_Hero:

    def __init__(self,name):
        self.name=name

    def super_power(self):
        self.context=["run","jump"]
        return self.context
    
class SpiderMan(Super_Hero):

    def super_power(self):
        self.context=super().super_power()
        self.context.append("fly")
        self.context.append("spread web")
        return self.context

class MinnalMurali(Super_Hero):

    def super_power(self):
        self.context=super().super_power()
        self.context.append("Speed")
        return self.context

obj1=SpiderMan("Spider-Man")
print(obj1.super_power())

obj2=MinnalMurali("Minnal Murali")
print(obj2.super_power())

# example