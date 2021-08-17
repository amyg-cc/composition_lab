class Band: 
    
    def __init__(self, name, musicians, manager):
        self.name = name
        self.musicians = musicians
        self.manager = manager

    def calculate_payroll(self):
        return self.manager.calculate_payroll(self.musicians)

    def pay_salaries(self):
        self.manager.pay_salaries(self.musicians)

    def play(self):
        playing = ""
        for musician in self.musicians:
            playing += musician.play() + "\n"
        return playing