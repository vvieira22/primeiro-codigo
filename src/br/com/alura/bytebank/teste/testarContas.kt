import br.com.alura.bytebank.modelo.Cliente
import br.com.alura.bytebank.modelo.ContaCorrente
import br.com.alura.bytebank.modelo.ContaPoupanca
import br.com.alura.bytebank.modelo.Endereco

fun testarContas() {

    var vitor = Cliente(
        nome = "Vitor",
        cpf = "11291292",
        senha = 9999,
        endereco = Endereco(
        logradouro = "Rua otavio pinheiro")
    )

    var thais = Cliente(
        nome = "Thais",
        cpf = "112915555292",
        senha = 999931312,
        endereco = Endereco()
    )

    var teste = Cliente(
        nome = "teste",
        cpf = "56112912292",
        senha = 1921999,
        endereco = Endereco()
    )

    var conta_vitor = ContaCorrente(
        titular = vitor,
        numeroConta = 1
    )
    var conta_thais = ContaPoupanca(
        titular = thais,
        numeroConta =  2
    )
    var conta_teste = ContaPoupanca(
        titular = teste,
        numeroConta =  3
    )

    conta_vitor.depositar(100.00)
    conta_vitor.transferir(10.00, conta_teste)
    println("logradouro:" + conta_vitor.titular.endereco)
    println(conta_vitor.saldo)

    conta_thais.depositar(100.00)
    conta_thais.transferir(10.00, conta_teste)
    println(conta_thais.saldo)
}





