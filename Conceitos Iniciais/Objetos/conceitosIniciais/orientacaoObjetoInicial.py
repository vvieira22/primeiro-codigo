def criar_conta(numero, titular, saldo):
    return {"numero" : numero, "titular": titular, "saldo": saldo}

def depositar(conta, valor):
    conta["saldo"] += valor

def sacar(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("O Saldo é: " + conta["saldo"])