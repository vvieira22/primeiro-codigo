package br.com.alura.bytebank.modelo

abstract class Conta(
    var titular: Cliente,
    var numeroConta: Int = 0
) : Autenticavel{
    var saldo = 0.0
        protected set

    override fun autentica(senha: Int): Boolean {
        return titular.autentica(senha);
    }

    //companion vai permitir que o objeto
    //seja compartilhado e ser membro da class
    //fazendo que só a classe faça modifcicacao nele
    companion object {
        var total = 0
            private set
    }

    init {
        total++
    }

    fun depositar(valor: Double) {
        saldo += valor
    }

    //deixar que cada filha faça seu saque da sua maneira.
    fun sacar(valor: Double) {
        if (saldo >= valor) {
            saldo -= valor
        }
    }

    abstract fun transferir(valor: Double, contaDestino: Conta, senha: Int)

}

