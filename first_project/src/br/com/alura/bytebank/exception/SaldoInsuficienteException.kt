package src.br.com.alura.bytebank.exception

import java.lang.Exception

class SaldoInsuficienteException(mensagem: String = "Saldo insuficiente.") : Exception(mensagem)
