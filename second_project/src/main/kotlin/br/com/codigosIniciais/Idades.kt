package br.com.codigosIniciais

fun main() {
    var idades = intArrayOf(12,20,30,7,29,55,21,20)

    for (idade in idades){
        println(idade)
    }

    val maiorIdade = idades.max()
    println("Maior idade: $maiorIdade")

    val menorIdade = idades.min()
    println("Menor idade: $menorIdade")

    val mediaIdades : String = String.format("%.3f", idades.average())
    println("Media idades: $mediaIdades")

    //retorna true se todos elementos do array satisfazerem a condição
    val saoMaioresDeIdade : Boolean = idades.all { it >= 18}
    println("Todos sao maiores de idade?: $saoMaioresDeIdade ")

    //verificar se apenas 1 no array satisfaz a condição:
    val ApenasUmMaiorDeIdade : Boolean = idades.any { it >= 18 }
    println("Algum aluno maior de idade?: $ApenasUmMaiorDeIdade ")

    //Pegar os valores e jogar numa lista, baseado na condição:
    val todosMaioresDeIdade : List<Int> = idades.filter { it >= 18 }
    println("Todos maiores de 18: $todosMaioresDeIdade")

    //Achar valor expecifico numa lista:
    //ele retorna o primeiro que achar, baseado na condição.
    val buscaNumero : Int? = idades.find { it >= 12 }
    println("NumeroEspecifico: $buscaNumero")
}
