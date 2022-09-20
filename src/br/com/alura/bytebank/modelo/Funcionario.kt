package br.com.alura.bytebank.modelo

abstract class Funcionario(
    var nome: String,
    var cpf: String,
    var salario: Double
) {

    fun alterar_salario(novo_salario: Double) {
        salario = novo_salario
    }

    abstract val bonificacao: Double


}