package src.br.com.alura.bytebank.exception

import java.lang.Exception

class FalhaAutenticacaoException(mensagem: String = "Autenticacao falhou") : Exception(mensagem)