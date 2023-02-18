package src.br.com.collections

fun main() {
    leituraMap()
    escritaMap()
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

    print(contas)
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