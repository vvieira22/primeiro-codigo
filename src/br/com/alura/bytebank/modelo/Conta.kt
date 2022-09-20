package br.com.alura.bytebank.modelo

abstract class Conta(
    var titular: Cliente,
    var numeroConta: Int = 0
) {
    var saldo = 0.0
        protected set

    //companion vai permitir que o objeto
    //seja compartilhado e ser membro daclass
    //fazendo que só a classe faça modifcicacao nele
    companion object {
        var total = 0
            private set
    }

    init {
        println("Conta criada!")
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

    abstract fun transferir(valor: Double, contaDestino: Conta): Boolean

}

