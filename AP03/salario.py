class Salario:
    def __init__(self, nome, salario, bonus, salariocombonus):
        self.nome = nome
        self.salario = salario
        self.bonus = bonus
        self.salariocombonus = salariocombonus
    def informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Salario: {self.salario}')
        print(f'Bonus: {self.bonus}%')
    def salario_total(self):
        self.salariocombonus = self.salario + (self.salario * self.bonus / 100)
        print(f'O salario total é de: {self.salariocombonus:.2f}')
pessoa1 = Salario('Mateus', 6000, 35, None)
pessoa1.informacoes()
pessoa1.salario_total()

pessoa2 = Salario('Thiago', 5523, 100, None)
pessoa2.informacoes()
pessoa2.salario_total()

pessoa3 = Salario('MouraDev', 3572 , 20, None)
pessoa3.informacoes()
pessoa3.salario_total()

pessoa4 = Salario('Felipe G', 19000, 10, None)
pessoa4.informacoes()
pessoa4.salario_total()
