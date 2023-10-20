class Employee:
    def __init__(self,name,salary,dept):
        self.name=name
        self.salary=salary
        self.dept=dept

    @property                           # @property access methode as property (it can use withiout parathesis () in the obj creation section)
    def get_name(self):
        return self.name
    
    @property                           # decorator
    def get_salary(self):
        return self.salary
    
emp=Employee("Hari",450000,"QA")
# print(emp.get_name())
print(emp.get_name)

# print(emp.get_salary())
print(emp.get_salary)