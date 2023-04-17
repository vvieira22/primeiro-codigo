import br.com.alura.bytebank.modelo.Cliente
import br.com.alura.bytebank.modelo.Conta
import br.com.alura.bytebank.modelo.ContaPoupanca
import br.com.alura.bytebank.modelo.Endereco as Enderec

fun main() {
    testaRun()

    somaReceiver(10,20, resultado = {
        println(this)
    })
}

fun testaRun() {
    val taxaAnual = 0.05
    val taxaMensal = taxaAnual / 12

    var contaPoupanca = Enderec(
        logradouro = "rua doutor celestino",
        numero = 310,
        bairro = "vila maicon douglas",
        cidade = "sao paulo",
        estado = "sp",
        cep = "25900182",
        complemento = "apartamento"
    ).let { endereco ->
        Cliente("vitor", "34252122769", endereco, 1234)
    }.let { cliente ->
        ContaPoupanca(cliente, 100)
    }

    contaPoupanca.run {
        depositar(3000.0)
        saldo * taxaMensal
    }.let { rendimentoMensal ->
        println("Rendimento mensal $rendimentoMensal")
    }

    val rendimentoAnual = run {
        var saldo = contaPoupanca.saldo
        repeat(12) { indice ->
            saldo += saldo * taxaMensal
        }
        saldo
    }
    println(rendimentoAnual)
}

fun testaWith() {
    val enderecoCompleto = with(Enderec())
    {
        logradouro = "rua doutor celestino"
        numero = 310
        bairro = "vila maicon douglas"
        cidade = "sao paulo"
        estado = "sp"
        cep = "25900182"
        complemento = "apartamento"
        enderecoCompleto()
    }.let(::println)
}

fun somaReceiver(a: Int, b: Int, resultado : Int.() -> Unit){
    println("antes da soma")
    val total = a + b
    total.resultado()
    println("depois da soma")
}
