package br.com.codigosIniciais

fun IterandoArray() {

    val salarios: DoubleArray = doubleArrayOf(
        1000.00,2000.00,5000.00,10000.00)

    val aumento = 1.1

    for(indice in salarios.indices) {
        salarios[indice] = salarios[indice] * aumento
    }
    println(salarios.contentToString())

    //alternativa
    salarios.forEachIndexed { i, salario ->
        salarios[i] = salario * aumento
    }
    println(salarios.contentToString())
}