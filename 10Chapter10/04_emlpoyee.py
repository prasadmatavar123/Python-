class Employee:
    company = "Google"

harry = Employee()
rajni = Employee()
harry.salary = 300
rajni.salary = 400
print(harry.company)
print(rajni.company)
Employee.company = "Youtube"
print(harry.company)
print(rajni.company)
print(harry.salary)
print(rajni.salary)    