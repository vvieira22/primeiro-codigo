class Data:
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
    def formatarDataSimples(self):
        return str(self.__dia) + "/" + str(self.__mes) + "/" + str(self.__ano)

data = Data(21,11,2007)
print(data.formatarDataSimples())