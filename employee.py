"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    totalPay = 0
    string = ""

    def __init__(self, name):
        self.name = name

    def get_pay(self):
        return Employee.totalPay

    def addToPay(amount):
        Employee.totalPay += amount

    def __str__(self):
        return self.name

    def editString(string):
        Employee.string = string

class SalaryEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(self,name)
        self.salary = salary
        self.addSalary()

    def getSalary(self):
        return self.salary

    def addSalary(self):
        Employee.addToPay(self.salary)

class ContractEmployee(Employee):
    salary = 0
    def __init__(self, name, rate, hours):
        super().__init__(self,name)
        self.rate = rate
        self.hours = hours

    def __str__(self):
        return (self.name + " works on a monthly salary of " + self.getSalary() +". Their total pay is " + self.get_pay() + ".")

    def calculateSalary(self):
        salary = self.rate * self.hours

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
