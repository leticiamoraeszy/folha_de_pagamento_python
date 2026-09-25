from abc import ABC
from rich import print

class Funcionario(ABC):
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base
        self.bonus_fixo = None
        

    def calcular_salario(self):
        pass

    def mostrar_salariobase(self):
        pass

class Gerente(Funcionario):
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)

    def calcular_salario(self, vendas, dias):
        self.dias = dias
        self.vendas_mes = vendas
        if 0 <= self.vendas_mes <= 5000:
            self.bonus_fixo = 0
        elif 5001 <= self.vendas_mes <= 20000:
            self.bonus_fixo = 1000
        else:
            self.bonus_fixo = 2000
        multi = self.vendas_mes * self.dias
        self.salario_base += multi 
        
    
    def mostrar_salariobase(self):
        print('----SALÁRIO BASE----')
        print(f'salário base de {self.nome} é de {self.salario_base}')
class Vendedor(Funcionario):
    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)

    def calcular_salario(self, vendas):
        self.vendas = vendas
        self.comissao = 0
        if 0 <=  self.vendas <= 500:
            self.comissao = 10
        elif 500 <= self.vendas <= 1000:
            self.comissao = 25
        else:
            self.comissao = 200
        self.salario_base += self.comissao

    def mostrar_salariobase(self):
        print('----SALÁRIO BASE----')
        print(f'salário base de {self.nome} é de {self.salario_base}')


c1 = Gerente(nome='Luiz', salario_base=1600)
c1.calcular_salario(vendas=2000, dias=25)
c1.mostrar_salariobase()
c2 = Vendedor(nome='João', salario_base=1200)
c2.calcular_salario(vendas=40)
c2.mostrar_salariobase()
        