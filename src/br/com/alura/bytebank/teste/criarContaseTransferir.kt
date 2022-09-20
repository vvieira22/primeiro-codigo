
import br.com.alura.bytebank.modelo.Cliente
import br.com.alura.bytebank.modelo.ContaCorrente
import br.com.alura.bytebank.modelo.ContaPoupanca
import br.com.alura.bytebank.modelo.Endereco
import src.br.com.alura.bytebank.exception.FalhaAutenticacaoException
import src.br.com.alura.bytebank.exception.SaldoInsuficienteException
import java.lang.Exception

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
    val contaAlex = ContaPoupanca(titular = alex,
        numeroConta = 1)
    val contaVitor = ContaCorrente(titular = vitor,
        numeroConta = 2)

//    contaAlex.depositar(100.00)
    contaVitor.depositar(1000.00)

    try {
        contaVitor.transferir(50.00, contaAlex, 1)
        println("Transferência realizada com sucesso")
    }
    catch (e: SaldoInsuficienteException) {
        println("saldo insuficiente!")
        e.printStackTrace()
    }
    catch (e: FalhaAutenticacaoException) {
        println("falha na autenticacao!!!")
        e.printStackTrace()
    }
    catch (e: Exception){
        println("ocorreu um erro desconhecido.")
        e.printStackTrace()
    }
    println(contaAlex.saldo)
    println(contaVitor.saldo)
}