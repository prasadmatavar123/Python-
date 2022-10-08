class Employee:
    company = "Google"
    def getSalary(self):
        print("Salary is 100k")

harry = Employee()
harry.getSalary()


# Next code

class Employee:
    company = "Google"
    def getSalary(self):
        print(f"salary is {self.salary}")

harry = Employee()
harry.salary = 100000
harry.getSalary()        
