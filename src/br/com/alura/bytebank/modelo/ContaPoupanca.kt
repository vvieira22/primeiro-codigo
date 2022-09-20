package br.com.alura.bytebank.modelo

class ContaPoupanca(
    titular: Cliente,
    numeroConta: Int
) : Conta(
    titular = titular,
    numeroConta = numeroConta
){
    var taxa_transferencia = 2.0
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

