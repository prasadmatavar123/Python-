class Person:
    country = "India"

    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.Salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am luckily breathing..")

class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to programmer")

p = Person()
p.takeBreath()
e = Employee()
e.takeBreath()
print(e.company)
pr = Programmer()              
pr.takeBreath()
print(pr.company) 
print(pr.country) 