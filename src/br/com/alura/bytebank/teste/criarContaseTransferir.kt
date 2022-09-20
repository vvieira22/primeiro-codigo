
import br.com.alura.bytebank.modelo.Cliente
import br.com.alura.bytebank.modelo.ContaCorrente
import br.com.alura.bytebank.modelo.ContaPoupanca
import br.com.alura.bytebank.modelo.Endereco

fun criarContaseTransferir() {

    var vitor = Cliente(
        nome = "Vitor",
        cpf = "11291292",
        senha = 9,
        endereco = Endereco()
    )

    var alex = Cliente(
        nome = "Alex",
        cpf = "11291292",
        senha = 1,
        endereco = Endereco()
    )
    val contaAlex = ContaPoupanca(titular = vitor,
        numeroConta = 1)
    val contaVitor = ContaCorrente(titular = alex,
        numeroConta = 2)

    if (contaVitor.transferir(50.00, contaAlex)) {
       println("Transferência realizada com sucesso")
    } else {
        println("Falha na transferência")
    }

    println(contaAlex.saldo)
    println(contaVitor.saldo)
}