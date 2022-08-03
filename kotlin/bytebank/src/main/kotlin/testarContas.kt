fun testarContas() {
    var conta_vitor = ContaCorrente(
        titular = "Vitor",
        numeroConta = 1,
        cpf = "12256122760"
    )
    var conta_thais = ContaPoupanca(
        titular = "Thais",
        numeroConta =  2,
        cpf = "120828920"
    )
    var conta_teste = ContaPoupanca(
        titular = "Teste",
        numeroConta =  3,
        cpf = "1202112828920"
    )

    conta_vitor.depositar(100.00)
    conta_vitor.transferir(10.00, conta_teste)
    println(conta_vitor.saldo)

    conta_thais.depositar(100.00)
    conta_thais.transferir(10.00, conta_teste)
    println(conta_thais.saldo)
}





