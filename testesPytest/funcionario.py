from datetime import datetime

class Funcionario:
    def __init__(self, nome, salario, data_nascimento):
        self._nome = nome
        self._salario = salario
        self._data_nascimento = data_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    @property
    def data_nascimento(self):
        return self._data_nascimento

    def idade(self):
        current_year = datetime.now().year
        return current_year - int((self.data_nascimento)[6:])
    
    def sobrenome(self):
        return self.nome.split()[-1]
    
    def reajuste_salarial_anual(self):
        self._salario *= 1.05
    
    #acima de 10000 nao recebe bonus, abaixo recebe 10% do salario
    def calcular_bonus_salarial(self):
        if self.salario < 10000:
            return self.salario * 0.1
        else:
            raise ValueError("Salario muito alto para receber o bonus")
    
    def __str__(self):
        return f"Funcionario: {self.nome}, Salario: {self.salario}, Data de Nascimento: {self.data_nascimento}"
