"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    totalPay = 0

    def __init__(self, name):
        self.name = name

    def get_pay(self):
        return self.totalPay

    def addToPay(self,amount):
        self.totalPay += amount

    def getSalary(self):
        return self.salary

class SalaryEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
        self.addToPay(self.salary)

    def __str__(self):
        return (self.name + " works on a monthly salary of " + str(self.getSalary()) +". Their total pay is " + str(self.get_pay()) + ".")


class ContractEmployee(Employee):
    salary = 0

    def __init__(self, name, rate, hours):
        super().__init__(name)
        self.rate = rate
        self.hours = hours
        self.calculateSalary()
        self.addToPay(self.salary)

    def calculateSalary(self):
        self.salary = self.rate * self.hours

    def __str__(self):
        return (self.name + " works on a contract of " + str(self.hours) + " hours at "+ str(self.rate) + "/hour. Their total pay is " + str(self.get_pay()) + ".")

class bonusSalaryEmployee(SalaryEmployee):
    commission = 0
    def __init__(self, name, salary, rate, contracts, bonus = True):
        super().__init__(name, salary)
        self.rate = rate
        self.contracts = contracts
        self.bonus = bonus
        self.calculateBonus()
        self.addToPay(self.commission)

    def calculateBonus(self):
        if self.bonus:
            self.commission = self.rate
        else:
            self.commission = self.rate * self.contracts

    def __str__(self):
        if self.bonus:
            return (self.name + " works on a monthly salary of " + str(self.getSalary()) +" and receives a bonus commission of " + str(self.commission) + ". Their total pay is " + str(self.get_pay()) + ".")
        else:
           return (self.name + " works on a monthly salary of " + str(self.getSalary()) +" and receives a commission for " + str(self.contracts) + " contract(s) at " + str(self.rate) + "/contract. Their total pay is " + str(self.get_pay()) + ".")

class bonusContractEmployee(ContractEmployee):
    commission = 0
    def __init__(self, name, rate, hours, cRate, contracts, bonus = True) :
        super().__init__(name, rate, hours)
        self.cRate = cRate
        self.contracts = contracts
        self.bonus = bonus
        self.calculateBonus()
        self.addToPay(self.commission)

    def calculateBonus(self):
        if self.bonus:
            self.commission = self.cRate
        else:
            self.commission = self.cRate * self.contracts

    def __str__(self):
        if self.bonus:
            return (self.name + " works on a contract of " + str(self.hours) + " hours at "+ str(self.rate) + "/hour and receives a bonus commission of " + str(self.cRate) + ". Their total pay is " + str(self.get_pay()) + ".")
        else:
            return (self.name + " works on a contract of " + str(self.hours) + " hours at "+ str(self.rate) + "/hour and receives a commission for " + str(self.contracts) + " contract(s) at " + str(self.cRate) + "/contract. Their total pay is " + str(self.get_pay()) + ".")



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = ContractEmployee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = bonusSalaryEmployee('Renee', 3000, 200, 4, False)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = bonusContractEmployee('Jan', 25, 150, 220, 3, False)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = bonusSalaryEmployee('Robbie', 2000, 1500, 0, True)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = bonusContractEmployee('Ariel', 30, 120, 600, 0, True)
