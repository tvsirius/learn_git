class House:
    def __init__(self, name, temp=20):
        self.name=name
        self.temp=temp
        self.condon=False
        self.hoton = False

    def cond(self, state=True):
        if state!=self.condon:
            self.condon = state
            if state:
                self.temp -= 10
            else:
                self.temp += 10

    def hot(self, state=True):
        if state!=self.hoton:
            self.hoton = state
            if state:
                self.temp += 10
            else:
                self.temp -= 10

    def __str__(self):
        return f'Дом {self.name}, температура = {self.temp}, кондиционер - {self.condon}, обогреватель - {self.hoton}'




