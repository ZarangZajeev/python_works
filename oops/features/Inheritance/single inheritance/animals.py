class Animal:
    name:str

    def __init__(self,name):
        self.name=name

    def sound(self):
        pass

class Dog(Animal):
    def sound(self):                                # method overring
        print(f"{self.name} sound is Barks")

    def __str__(self):
        return self.name

class Frog(Animal):
    def sound(self):
        print(f"{self.name} sound is croaks")

    def __str__(self):
        return self.name

obj1=Dog("DOG")
obj1.sound()
print(obj1)

obj2=Frog("FROG")
obj2.sound()
print(obj2)




print(obj1.__class__)       # Which class, it is an attribute
print(obj1.__class__.__class__)