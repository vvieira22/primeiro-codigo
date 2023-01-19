package br.com.lists

data class Prateleira (
    val genero : String,
    val livros: List<Livro>
)
{
    fun organizarPorAutor(): List<Livro> {
        return livros.sortedBy { it.nomeAutor }
    }

    fun organizarPorAno() : List<Livro> {
        return livros.sortedBy { it.anoPublicacao }
    }
}