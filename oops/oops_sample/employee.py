class Employee:
    id:int
    name:str
    dept:str
    salary:int
    company:str="IBM"

    def set_employee(self,id,name,dept,salary):
        self.id=id
        self.name=name
        self.dept=dept
        self.salary=salary

    def display(self):
        print(self.id,self.name,self.dept,self.salary,Employee.company)

    def __str__(self):
        return self.name


# refference name= ClassName()
emp1=Employee()
emp1.set_employee(101,"Fayas","Android",45000)
emp1.display()
print(emp1)

emp2=Employee()
emp2.set_employee(102,"Aravind","Python",44000)
emp2.display()