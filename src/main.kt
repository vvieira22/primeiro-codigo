import br.com.alura.bytebank.modelo.Conta
import br.com.alura.bytebank.modelo.Endereco
import src.br.com.alura.bytebank.modelo.Teste

fun main() {
//    a classe abstrata serve como base
//    para a gente representar
//    apenas, como por exemplo funcionario
//    não existe cargo funcionario, existe analista etc..
//    so servir como base, nao pode ser usado.
//    Abstract já é classe aberta
//ao criar um mebro abstrado é necessário que os filhos
    //tenham esse método implementado.
//Interface é abstrata
    //interface nao mantem valor das variaveis(status)
    //construtor nao existe em interface.
    //interface nao vai ter o vinculo todo igual herença
    // interface = contrato, quem usa tem que implementar.


//    testarContas()
//    criarContaseTransferir()
//    println("contas: ${Conta.total}")
//
//    val teste = Endereco()
//    var numero = 10;

val teste = Teste("maria", 10)
val (nome, idade) = teste
println("$nome\n$idade")
}





