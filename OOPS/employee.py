class Employee:
    company = "Whatsapp"
    def getSalary(self):
        print(f"the salary of  is 1000")
    def dept(self):
        print("the depart is CSE")

            

disha = Employee()
subha = Employee()
subha.getSalary()
disha.dept()
print(subha.company)
subha.salary = 100000000 #isinstance variable 
print(subha.salary)