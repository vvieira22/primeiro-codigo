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

    /*
    apply e also : Retorna o contexto do objeto
    let, run e with: Retorna o resultado da lambda anterior (no caso a ultima expressao realizada)

    *Let
    Objeto de contexto (it), retorno lambda.

    *With
    Nao é uma funcao de extensão. Tem que mandar como parametro
    entre (). Objeto de contexto é (this), e o resultado é lambda.
    O uso se da por, pegar um objeto, trabalhar com seus elementos,
    de tal forma que você ou não quer devolver nada ou quer devolver algum calculo.

    *Run
    Função de extensão ou não, Objeto de contexto (this), e o retorno é lambda.
    Podemos rodar run sem necessiaramente depender de um objeto.

    *Apply
    Objeto de contexto devolvendo (this). O retorno é o próprio objeto.
    "Aplique as atribuicoes para o objeto." Criei um objeto e quero adicionar
    coisas a mais nele, temos com apply e adicionamos coisas e ele retorna
    um objeto novo atualizado. "Configurar objeto".

    *Also
    Objeto de contexto devolvendo (this). O retorno é o próprio objeto.
    Ele é bom para fazer açoes quando tem o objeto de contexto. Ele não tem
    efeitos colaterais no código, bom para fazer logs.


    //true e false.
    *takelf == verdadeiro, devolve objeto
    *takeUnless == falso, devolve objeto
    */

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