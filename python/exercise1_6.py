class Employee:
    name = ''
    hourly_rate = 0
    contract_hours = 0
    monthly_salary = 0
    commission_rate = 0
    contracts = 0
    bonus_commission = 0
    total_pay = 0

    def __init__(self, name):
        self.name = name

    def set_hourly_rate(self, rate):
        self.hourly_rate = rate

    def set_contract_hours(self, hours):
        self.contract_hours = hours

    def set_monthly_salary(self, salary):
        self.monthly_salary = salary

    def set_contracts(self, contracts):
        self.contracts = contracts

    def set_commission_rate(self, rate):
        self.commission_rate = rate

    def set_bonus_commission(self, bonus_comm):
        self.bonus_commission = bonus_comm

    def calculate_total_pay(self):
        if(self.total_pay != 0):
            return
        if self.hourly_rate and self.contract_hours:
            self.total_pay += self.hourly_rate * self.contract_hours
        if self.monthly_salary:
            self.total_pay += self.monthly_salary
        if self.commission_rate and self.contracts:
            self.total_pay += self.commission_rate * self.contracts
        if self.bonus_commission:
            self.total_pay += self.bonus_commission

    def get_pay(self):
        self.calculate_total_pay()
        # print(self.total_pay)
        return self.total_pay

    def __str__(self):
        str = '{self.name} works on a '
        if self.monthly_salary:
            str += 'monthly salary of {self.monthly_salary}'
        if self.hourly_rate and self.contract_hours:
            str += 'contract of {self.contract_hours} hours at {self.hourly_rate}/hour'
        if self.commission_rate and self.contracts:
            str += ' and receives a commission for {self.contracts} contract(s) at {self.commission_rate}/contract'
        if self.bonus_commission:
            str += ' and receives a bonus commission of {self.bonus_commission}'

        str += '. Their total pay is {self.total_pay}.'

        print(str.format(self=self) + '\n')


# Billie works on a monthly salary of 4000. Their total pay is 4000.
billie = Employee('Billie')
billie.set_monthly_salary(4000)
billie.get_pay()
billie.__str__()

# Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500.
charlie = Employee('Charlie')
charlie.set_hourly_rate(25)
charlie.set_contract_hours(100)
charlie.get_pay()
charlie.__str__()
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800.
renee = Employee('Renee')
renee.set_monthly_salary(3000)
renee.set_contracts(4)
renee.set_commission_rate(200)
renee.get_pay()
renee.__str__()

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410.
jan = Employee('Jan')
jan.set_hourly_rate(25)
jan.set_contract_hours(150)
jan.set_contracts(3)
jan.set_commission_rate(220)
jan.get_pay()
jan.__str__()

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500.
robbie = Employee('Robbie')
robbie.set_monthly_salary(2000)
robbie.set_bonus_commission(1500)
robbie.get_pay()
robbie.__str__()

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200.
ariel = Employee('Ariel')
ariel.set_hourly_rate(30)
ariel.set_contract_hours(120)
ariel.set_bonus_commission(600)
ariel.get_pay()
ariel.__str__()