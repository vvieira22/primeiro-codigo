#1
class Estatistica:
    def __init__(self, idades : list):
        self.idades = idades
    def media(self):
        return sum(self.idades) / len(self.idades)
    def mediana(self):
        lista = sorted(self.idades)
        if len(lista) % 2 == 0:
            return (lista[len(lista) // 2] + lista[len(lista) // 2 - 1]) / 2
        else:
            return lista[len(lista) // 2]
    def moda(self):
        lista = sorted(self.idades)
        return max(lista, key=lista.count)
    def variancia(self):
        media = self.media()
        return sum((x - media) ** 2 for x in self.idades) / len(self.idades)
    def desvioPadrao(self):
        return self.variancia() ** 0.5
    def coeficienteDeVariacao(self):
        return self.desvioPadrao() / self.media()
    def describe(self):
        print("Média: ", self.media())
        print("Mediana: ", self.mediana())
        print("Moda: ", self.moda())
        print("Variância: ", self.variancia())
        print("Desvio Padrão: ", self.desvioPadrao())
        print("Coeficiente de Variação: ", self.coeficienteDeVariacao())

stst = Estatistica([31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26])
print("Mean: ", stst.media())
print("Median: ", stst.mediana())
print("Mode: ", stst.moda())
print("Variance: ", stst.variancia())
print("Standard Deviation: ", stst.desvioPadrao())
print("Coefficient of Variation: ", stst.coeficienteDeVariacao())
stst.describe()


#2
class PersonAccount:
    def __init__(self, name, sobrenome, receita, despesas):
        self.name = name
        self.sobrenome = sobrenome
        self.receita = receita
        self.despesas = despesas
    def total_expenses(self):
        return sum(self.despesas)
    def add_income(self, income):
        self.receita.append(income)
    def add_expense(self, expense):
        self.despesas.append(expense)
    def account_balance(self):
        return sum(self.receita) - sum(self.despesas)