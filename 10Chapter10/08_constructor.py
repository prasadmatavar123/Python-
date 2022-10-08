class Employee:
    company= "Google"

    def __init__(self,name,salary,subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!")
        

        def getSalary(self,signature):
            print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

        @staticmethod
        def greet():
            print("Good Morning,sir")

        @staticmethod
        def time():
            print("The time is 9AM in the morning")

harry = Employee("Harry",100,"Youtube")