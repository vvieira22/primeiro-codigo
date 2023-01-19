package br.com.lists

fun main() {

    //AGRUPAR LIVROS POR EDITORA.
    listaDeLivros
            .groupBy { it.editora ?: "Editora Sem nome"  }
            //elvis operator, para renomear caso encontramos algum
            //elemento nulo a esquerda.
            .forEach { (editora : String, livros : List<Livro>) ->
                println("$editora: ${livros.joinToString { it.nomeLivro }}")
            }
}