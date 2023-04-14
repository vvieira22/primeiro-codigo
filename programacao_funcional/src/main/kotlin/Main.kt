import java.util.*

class Endereco (
    var lagradouro: String = "",
    var numero: Int = 0,
)
//Precisa disso pra saber como Endereco deve ser imprimido.
//se nao vai sempre imprimir o endereço de memória do objeto nele setado.
{
    override fun toString(): String {
        return  "Logradoro:   $lagradouro\n" +
                "Numero:      $numero\n"
    }
}

fun main(args: Array<String>) {

    val endereco = Endereco(lagradouro = "rua doutor celestino", numero = 310)
    val enderecoMaisculo = "${endereco.lagradouro}, ${endereco.numero}".toUpperCase()
    println(enderecoMaisculo)

    //A diferença usando esse código de cima com high order function
    // e que vc nao precisaria declarar essas variaveis e atribuir:.
    val enderecoemMaisculo = Endereco(lagradouro = "rua doutor celestino", numero = 310)
        .let{ endereco ->
            "${endereco.lagradouro}, ${endereco.numero}".toUpperCase()
        }
    println(enderecoemMaisculo)

    //Eu ainda posso encadear esse let em outro let, o retorno vai virar o let.
    Endereco(lagradouro = "rua doutor celestino", numero = 310)
        .let{ endereco ->
            "${endereco.lagradouro}, ${endereco.numero}".toUpperCase()
        }.let{ enderecoEmMaisculo ->
            // aqui ja tem o retorno completo em string.
            println(enderecoEmMaisculo)
        }

    //melhorar ainda mais, facilitando a impressao:
    Endereco(lagradouro = "rua doutor celestino", numero = 310)
        .let{ endereco ->
            "${endereco.lagradouro}, ${endereco.numero}".uppercase()
        }.let(::println)

    listOf(Endereco(lagradouro = "rua doutor x"),
        Endereco(),
        Endereco(lagradouro = "rua doutor y", numero = 999))
        .filter { endereco ->
            endereco.lagradouro.isNotEmpty() && endereco.numero > 0}
        .let(::println)

    soma(1,5) {
        //so  vai funcionar assim que chamar a fucao interna resultado
        //lazy evaluation, muito comum para usar com eventos de click etc..
        println(it)
    }
}
fun soma(a : Int, b: Int, resultado : (Int) -> Unit) {
    println("antes da soma")
    resultado( a + b)
    println("depois da soma")
}