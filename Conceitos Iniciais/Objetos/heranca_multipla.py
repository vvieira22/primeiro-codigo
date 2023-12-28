#O EXEMPLO DE HERANÇA MÚLTIPLA SE BASEA NA IMAGEM "empresa.png"

class Pessoa:
    def __init__(self, nome, cpf, idade):
        self._nome = nome
        self._cpf = cpf
        self._idade = idade

#classes mixin, quando uma classe não tem nada instanciada, 
#só faz uma coisa muito específica que pode ser usada por outras exemplo:
#interessante usar para log, de horas, nao preciso vir em cada classe e implementar a class que gera log.
class FuncionarioGeek():
    def __str__(self):
        return "funcionario Geek"

class Socio(Pessoa):
    def __init__(self,nome, cpf, idade, id_socio, capital_investido, area_atuacao):
        super().__init__(nome, cpf, idade)
        self._id_socio = id_socio
        self._capital_investido = capital_investido
        self._area_atuacao = area_atuacao

#funções fictícias utilizadas para exemplo de acesso.
    def ultimo_capital_empresa(self):
        return 1000000
    def numero_de_funcionarios(self):
        return 548

class DiretorInvestidor(Socio, FuncionarioGeek):
    def __init__(self, nome, cpf, idade, id_socio, capital_investido, area_atuacao): 
        super().__init__(nome, cpf, idade, id_socio, capital_investido, area_atuacao)

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, idade, id_funcionario, setor):
        super().__init__(nome, cpf, idade)
        self._id_funcionario = id_funcionario
        self._setor = setor

vitor = DiretorInvestidor("vitor", "123", "20", "001", "100000R$", "tecnologia")
print(vitor)