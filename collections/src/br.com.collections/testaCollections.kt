private fun testaCopia() {
    val bancoDeNomes = BancoNomes()

    /*
      Passagem de valor de uma Collection para outra.
    Evita referencia, cada "objeto" vai ser único, cada cópia vai ser única.
      Tanto que o hash fica diferente se feito dessa forma
    */
    val bancoDeNomesCopia = bancoDeNomes.nomes.toMutableList()
    println(bancoDeNomes.hashCode())
    println(bancoDeNomesCopia.hashCode())

    bancoDeNomes.salvaNome("Beatriz")
    println(bancoDeNomesCopia)

//    Mesmo se a gente instanciar outro objeto o valor vai ser mantido.
//    Por causa do Companion Object.
    println(BancoNomes().nomes)
}

class BancoNomes {

    val nomes: Collection<String> get() = Companion.dados

    fun salvaNome(nome: String){
        Companion.dados.add(nome)
    }

    /*
    Um Companion Object em Kotlin é um objeto estático associado a uma classe.
    É semelhante a uma classe estática em Java. Ele pode acessar todas as propriedades
    e funções da classe sem precisar instanciá-la. É definido com a palavra-chave
    "companion" na classe. Ele é útil para compartilhar funcionalidades entre várias
    instâncias de uma classe ou para criar constantes na classe.
     */

    companion object {
        private val dados = mutableListOf<String>()
    }

}

fun testaColecao() {
    val nomes: Collection<String> = mutableListOf(
        "Alex",
        "Maicon",
        "Thaina",
        "Juliana"
    )

    for (nome in nomes) {
        println(nome)
    }
    println("Tem o nome Maicon?: ${nomes.contains("Maicon")}")
    println("Tamanho da colecao: ${nomes.size}")
}
