package br.com.alura.bytebank.modelo

import src.br.com.alura.bytebank.exception.FalhaAutenticacaoException
import src.br.com.alura.bytebank.exception.SaldoInsuficienteException

class ContaCorrente(
    titular: Cliente,
    numeroConta: Int
) : Conta(
    titular = titular,
    numeroConta = numeroConta
){
    var taxa_transferencia = 1.0
        private set

    override fun transferir(valor: Double, contaDestino: Conta, senha: Int) {

        if (!autentica(senha)){
            throw FalhaAutenticacaoException();
        }

        if (super.saldo >= valor + taxa_transferencia) {
            super.saldo -= valor - taxa_transferencia
            contaDestino.depositar(valor)
        }
        else
        {
            throw SaldoInsuficienteException("Saldo insuficiente, valor atual do saldo:"+ super.saldo);
        }
    }
}

