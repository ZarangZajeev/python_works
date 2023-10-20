# Abstraction : Abstraction in Python is a process of hiding the implementation details of a class and
# exposing only the essential details to the user


from abc import ABC,abstractmethod

class Editor(ABC):

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def debug(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def save(self):
        pass

class VsCode(Editor):
    def edit(self):
        print("VS code Edit")

    def debug(self):
        print("VS code debug")

    def run(self):
        print("VS code run")

    def save(self):
        print("VS code save")

obj=VsCode()
obj.edit()