# salaryAfterIncrement = salary * increment 

class Employee:
    salary = 1000
    increment = 1.5
    @property
    def salaryAfterIncrement(self):
        return self.salary * self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sai):
        self.increment = sai/self.salary

e = Employee()
print(e.salaryAfterIncrement)        
           