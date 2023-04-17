fun main()
{
    testeTipoFuncaoClassEreferencial();
    testaLambdaEFuncaoAnonima();
}

fun testaLambdaEFuncaoAnonima() {
    //nao da pra reutilizar como variavel, tanto lambda quanto anonima
    val minhaFuncaoLambda = {
        println("minha impressao lambda")
    }

    val minhaFuncaoAnonima : () -> Unit = fun() {
        println("minha impressao Anonina")
    }


    //lambda usando parametros
    //Podemos substituir o a ou b, pelo caractere _
    //significa que é um parametro que vc n vai usar, MAS PRECISA DECLARAR.
    //a expressao lambda retorna sempre a ultima expressao
    val minhaFuncaoLambda2 : (Int, Int) -> Int = { a, b ->
        println("minha funcao lambda 2")
        a+b
    }
    println(minhaFuncaoLambda2(10,25));

    //Tambem podemos inferir direto no parametro o seu tipo.
//    val minhaFuncaoLambda2 = { a : Int, b : Int ->
//        a+b
//    }

    //A difereça entre usar lambda ou funcao anoninma, é que a anonima
    //garante um escopo certinho forçando a declaracao de retorno, mais explicita que a lambda.
    //Embora a funcao lambda predomine entre códigos kotlin.
    val minhaFuncaoAnonima2 = fun(a : Int, b : Int) : Int {
        println("minha funcao anonima 2")
        return a + b
    }
    println(minhaFuncaoAnonima2(30,30))

    //Funcao lambda com 1 parametro, it é acessível.
//    val calculaBonificacao : (Double) -> Double = {
//        it + 100.00
//    }
//    println(calculaBonificacao(2000.00))

    //assim a gente consegue retornar por label, em vez de cair direto no ultimo retorno ele vai retornar primeiro
    //se cair na primeira expressao do if.
    val calculaBonificacao : (salario:Double) -> Double = lambda@{ salario ->
        if(salario > 3000.00)
        {
            return@lambda salario + 50
        }

        salario + 100.00
    }
    println(calculaBonificacao(2000.00))

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
    val minhaFuncaoClass : (Int,Int)  -> Int = Teste()
    println(minhaFuncaoClass(10, 10))
}
fun retorna1Numero(numero : Int) : Int{
    println("chamou aq")
    return numero;
}
class Teste : (Int, Int) -> Int {
    // retorno da funcao pode ser em bloco normal { } ou em expressao (assim), pra facilitar
    override fun invoke(p1: Int, p2: Int): Int = p1 + p2
}