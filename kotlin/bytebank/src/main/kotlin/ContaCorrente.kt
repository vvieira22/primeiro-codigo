class ContaCorrente(
    titular: String,
    numeroConta: Int,
    cpf: String
) : Conta(
    titular = titular,
    numeroConta = numeroConta,
    cpf = cpf
){
    var taxa_transferencia = 1.0
        private set

    override fun transferir(valor: Double, contaDestino: Conta): Boolean {
        if (super.saldo >= valor + taxa_transferencia) {
            super.saldo -= valor - taxa_transferencia
            contaDestino.depositar(valor)
            return true
        }
        return false
    }
}

