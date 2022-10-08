class Employee:
    company = "Google"

    def getSalary(self,signature):
        print(f"Salary for this employee working in {self.company}\n {signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

harry = Employee()
harry.salary = 100000
harry.getSalary("Thanks!") #Employee.getSalary(harry)
harry.greet() # Employee.greet()           