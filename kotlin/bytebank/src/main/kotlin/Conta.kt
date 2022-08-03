abstract class Conta(
    var titular: String,
    var numeroConta: Int = 0,
    var cpf: String
) {
    var saldo = 0.0
        protected set

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

