package br.com.codigosIniciais.testes

fun MenorEmaiorArray() {
    val idades: IntArray = intArrayOf(
        10,5,1,30
    )

    var menorIdade: Int
    var maiorIdade: Int

    menorIdade = Int.MAX_VALUE
    maiorIdade = idades.max()

    idades.forEach { idade ->
        if( idade < menorIdade){
            menorIdade = idade
        }
    }
    println("menor idade $menorIdade")
    println("maior idade $maiorIdade")

}