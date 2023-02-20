fun main() {
    val contas = listOf<Conta>(
            Conta("Pedro", 501.00),
            Conta("Marcos", 20000.22234),
            Conta("Jose", 0.0)
        )
//    println(contas)

    val contasMapeadas : Map<String, Double> =
            contas.associate { conta : Conta ->
                Pair(conta.nome, conta.valor)
    }

    //transforma o valor em chave para um novo mapa
    val contasPremium = contas.associateWith { pedido ->
        pedido.valor >= 100.00
    }
//    println(contasPremium)
//    println(contasPremium[Conta(nome="Pedro", valor=501.0)])

    //Usando o groupby, faz mais sentido e é mais usual
    val contasAtivas : Map<Boolean, List<Conta>> = contas.groupBy { contas ->
        contas.valor > 0.0
    }
    //ele vai agrupar beseado na condicao, no caso a condicao é boolean
    println(contasAtivas)

    //Podemos agrupar em estilo agenda.
    val nomes = listOf(
            "vitor",
            "mariana",
            "paulo",
            "thiago",
            "mario",
            "vitoria",
            "maicon"
    )
    println(nomes.groupBy { nome ->
        nome.first()
    })


}
data class Conta(val nome:String, val valor: Double)

