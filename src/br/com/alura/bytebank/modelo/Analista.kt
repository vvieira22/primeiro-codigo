package br.com.alura.bytebank.modelo

class Analista(
    nome: String,
    cpf: String,
    salario: Double
) : Funcionario(
    nome = nome,
    cpf = cpf,
    salario = salario
) {

    //força modificar a bonificacao original
    override val bonificacao: Double get() =  salario * 0.15

}