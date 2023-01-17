package br.com.lists

/*
DATA CLASS
Tipo especial de class em kotlin
fornece caracteristias e metodos a mais automaticamente
 */

data class Livro  (
    val nomeAutor: String,
    val nomeLivro: String,
    val anoPublicacao: Int,
    val Editora:String? = null
): Comparable<Livro> {
    override fun compareTo(other: Livro): Int {
        return this.anoPublicacao.compareTo(other.anoPublicacao)
    }
}