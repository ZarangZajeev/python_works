class Editor():
    name:str
    def __init__(self,name):
        self.name=name

    def spec(self):
        pass

class VsCode(Editor):
    def spec(self):
        print(f"{self.name} supports edit, debug, run and extension support")

    def __str__(self):
        return self.name
    
class Pycharm(Editor):
    def spec(self):
        print(f"{self.name} supports run, debug, edit")

    def __str__(self):
        return self.name
    
vsobj=VsCode("VsCode")
vsobj.spec()
print(vsobj)

pyobj=Pycharm("Pycharm")
pyobj.spec()