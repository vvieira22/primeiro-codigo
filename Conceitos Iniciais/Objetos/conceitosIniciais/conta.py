class Conta:
    #Construtor
    def __init__(self, numero_conta = None, nome_titular = None, saldo = None):
        self.__numero_conta = numero_conta
        self.__nome_titular = nome_titular
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            return True
        return False

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    def __pode_sacar(self, valor_a_sacar):
        return self.__saldo >= valor_a_sacar

    @property
    def numero_conta(self):
        return self.__numero_conta

    @property
    def nome_titular(self):
        return self.__nome_titular
        
    @nome_titular.setter
    def nome_titular(self, novo_nome):
        self.__nome_titular = novo_nome

    #É usado para ocultar a funcionalidade interna de qualquer classe do mundo externo.
    #Métodos privados são aqueles métodos que não devem ser acessados ​​fora da 
    # classe nem por nenhuma classe base. Sempre começam com __ para "mascarar"
    def __metodo_privado(self):
        return True


    # Já os métodos estáticos utilizamos quando não precisamos receber a 
    # referência de um objeto especial (seja da classe ou de uma instância) 
    # e funciona como uma função comum, sem relação.

    # Quando definimos um método estático, ou seja, de classe, 
    # podemos chamá-lo sem a necessidade de criação de um objeto antes.        
    @staticmethod
    def metodo_estatico():
        return True