package br.com.lists

fun main(){

val livro1 = Livro(
    "Maicon Douglas",
    "Em busca da depressão 1",
    2021,
    "Intrisica"
)
val livroExtra = Livro(
    "Maicon Douglas",
    "Em busca da depressão 2",
    2023,
    "Intrisica"
)

val livro2 = Livro(
    "Guimarães Rosa",
    "Grande Sertão: Veredas",
    1900,
    "Áurea"
)
val livro3 = Livro(
    "Helena Morley",
    "Minha vida de menina",
    2020,
    "Abril"
)
val livro4 = Livro(
    "Machado de Assis",
    "Memórias Póstumas de Brás Cubas",
    1881,
    "Editora Brasil"
)

val livros : MutableList<Livro> =
        mutableListOf(
            livro1,
            livroExtra,
            livro2,
            livro3
        )

//consigo adicionar elementos numa lista, pois são mutáveis != arrays
livros.add(livro4)

//remover elemento da lista
//livros.remove(livro4)

//implementação like a bross
livros.imprimeComMarcadores()
val livroOrdenados: List<Livro> = livros.sorted()
livroOrdenados.imprimeComMarcadores()

//facilitando ordenação baseado no critério, modo fácil
val livroOrdenadosPorAnoPublicacao = livros.sortedBy { it.anoPublicacao }


//Filtrando livros
val filtroLivrosComRetornoPorString =
livros
    .filter { it.nomeAutor == "Maicon Douglas" }
    .sortedBy { it.anoPublicacao }
    .map { it.nomeLivro }
println(filtroLivrosComRetornoPorString)
//    A função map irá criar uma lista nova contendo os elementos retornados
//    pela função ou expressão passada entre as chaves
}

fun List<Livro>.imprimeComMarcadores(){
    val textoFormatado = this.joinToString(separator = "\n") {
        " - ${it.nomeLivro} de ${it.nomeAutor}"
    }
    println("--Lista de Livros ---")
    println(textoFormatado)
}

