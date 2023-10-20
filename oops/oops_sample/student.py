class Student:
    rol:int
    course:str
    total:int

    def __init__(self,rolnum,course,total):
        self.rol=rolnum
        self.course=course
        self.total=total
    def display(self):
        print(self.rol,self.course,self.total)

stu1=Student(34,"Python",450)
stu1.display()