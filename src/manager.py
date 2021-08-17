class Manager: 
    
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def calculate_payroll(self, musicians):
        payroll = 0
        for musician in musicians:
            payroll += musician.get_salary()
        return payroll

    def pay_salaries(self, musicians):
        for musician in musicians:
            musician.add_money(musician.salary)