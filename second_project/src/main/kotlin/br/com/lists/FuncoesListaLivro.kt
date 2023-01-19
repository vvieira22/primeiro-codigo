package br.com.lists

fun List<Livro?>.imprimeComMarcadores() {
    val textoFormatado = this
            .filterNotNull()
            .joinToString(separator = "\n") {
                " - ${it.nomeLivro} de ${it.nomeAutor}"
            }
    println("--Lista de Livros ---")
    println(textoFormatado)
}