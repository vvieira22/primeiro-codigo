package src.br.com.collections

fun main() {
//    leituraMap()
    escritaMap()
//    testaExcecoes()
//    testaFiltro()
}

private fun escritaMap() {
    val contas: MutableMap<String, Double> = mutableMapOf(
        Pair("Maicon", 20.0),
        "Jose" to 2.120,
        Pair("Leandro", 500.0)
    )

    //inserir no dicionario, duas formas:
    contas["vitor"] = 500.00
    contas.put("vitor", 500.00)
    //como é dicionario, n vai inserir 2x, apenas 1 key é permitida.

    //Pra atualizar o valor é a mesma forma, ele vai substuir o valor original
    contas.put("vitor", 60000.00)

    //Cria se nao existe, se existe nao faz nada..
    contas.putIfAbsent("vitor", 50000.0000)

    //remover elemento baseado na chave
    contas.remove("vitor")

    //remove elemento com a condicao de chave + valor = true.
    contas.remove("vitor", 60000.00)

    //Operador + e - usando mapas
    println(contas + Pair("teste", 100.00))
    println(contas + mapOf("vitoor" to 10.0, "testee" to 20.000))

    println(contas - "Maicon")
    println(contas - listOf("Maicon", "Jose"))

    //esse metodo sobreescreve tudo, meio que vai colocar um mapa inteiro dentro da atual, se tiver igual ele sobreescreve.
    contas.putAll(mapOf("vitoor" to 10.0, "testee" to 20.00))
    //ou simplemnete fazer usando operador +=
    contas += mapOf("vitoor" to 10.0, "testee" to 20.00)


    //Opcoes especiais para remocao

    println(contas)

    //remover pelo valor especifico, vai remover primeiro que ele ahcar
    contas.values.remove(20.00)

    //usando operador -= pra remover
    contas -= "Jose"
    println(contas)

}

fun leituraMap() {
    val contas: Map<String, Double> = mapOf(Pair("Maicon", 20.0), "Jose" to 2.120, Pair("Leandro", 500.0))

    val saldoMaicon: Double? = contas["Maicon"]
    saldoMaicon?.let {
        println("conta: $it")
    }

    for (conta in contas) {
        println("\nSaldo ${conta.key}\n Saldo: ${conta.value}\n")
    }
}

fun testaExcecoes() {
    val contas: Map<String, Double> = mapOf(Pair("Maicon", 20.0), "Jose" to 2.120, Pair("Leandro", 500.0))

    //pegue o valor da conta, caso contrario faça o que a expressao lambida disser.
    println(contas.getOrElse("Thiago")
    {
        "Nao achou Thiago"
    })
    //pegue o valor da conta, ou retorne algo padrao
    println(contas.getOrDefault("Thiago", 20.00))

}

fun testaFiltro() {
    val contas: Map<String, Double> = mapOf(Pair("Amarildo", 20.0), "Jose" to 2.120, Pair("Amianto", 500.0))

    //Cria um filtro que retorna um novo mapa se o nome da chave começar com A e o valor da chave for >= 100.00
    val filtro = contas.filter { (nome : String, saldo: Double) ->
        nome.substring(0,1) == "A" && saldo >= 100.00
    }
    //Podemos ter filterValues e filterKeys que n precisam descrever toda declaracao do mapa original
    print(filtro)
}