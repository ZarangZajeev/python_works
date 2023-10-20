# Inheritance


class Parent:

    def mobile(self):
        print("Samsung M32")

    def bike(self):
        print("passion pro")

class Child(Parent):
    pass

obj1=Child()
obj1.mobile()
obj1.bike()


