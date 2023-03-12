fun main()
{
//    testeTipoFuncaoClassEreferencial();

    //nao da pra reutilizar como variavel, tanto lambda quanto anonima
    val minhaFuncaoLambda = {
         println("minha impressao lambda")
    }

    val minhaFuncaoAnonima : () -> Unit = fun() {
         println("minha impressao lambda")
    }
}

fun testeTipoFuncaoClassEreferencial() {

//    val minhaFuncao : () -> Unit
//    parenteses significa os parametros que podemos receber do tipo funcao
//     -> significa retorno, sempre vai exigir um retorno

//    println(minhaFuncao)

//O codigo acima nao funciona pois precisa que a funcao tenha um assinatura, que seja compativel
// com a funcao definida
//abaixo está o modelo implementado corretamente.

    val minhaFuncao : (numero : Int) -> Int = ::retorna1Numero
    // :: ta mandando a referencia da funcao e n a execucao dela.
    //tanto que mesmo dando print nela, ele n vai mostrar "chamou aq"
    //lazy evaluation.
    println(minhaFuncao)

    //agora ele executa
    println(minhaFuncao(1))


    //da pra fazer usando classes tambem
    val minhaFuncaoClass : () -> Unit = Teste()
}
fun retorna1Numero(numero : Int) : Int{
    println("chamou aq")
    return numero;
}

class Teste : () -> Unit {
    override fun invoke() {

        println("roda invoke do teste")
    }
}