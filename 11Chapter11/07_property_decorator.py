class Employee:
    company = "Bharat Gass"
    salary = 5600
    salarybonus = 400
    # totalSalary = 6100

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

        @totalSalary.setter
        def totalsalary(self,val):
            self.salarybonus = val - self.salary

e = Employee()
print(e.totalSalary)   
print(e.salary)
print(e.salarybonus) 
e.totalsalary = 5800
