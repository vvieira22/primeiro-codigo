package br.com.lists

fun main() {

    //consigo adicionar elementos numa lista, pois são mutáveis != arrays
//    listaLivros.add(Livro)

    //remover elemento da lista
    //listaLivros.remove(livro)

    //implementação like a bross
//    listaLivros.imprimeComMarcadores()
    val livroOrdenados: List<Livro> = listaDeLivros.sorted()
//    println("Livros Ordenados:")
//    livroOrdenados.imprimeComMarcadores()

    //facilitando ordenação baseado no critério, modo fácil
    val livroOrdenadosPorAnoPublicacao = listaDeLivros.sortedBy { it.anoPublicacao }

    //Filtrando livros
    val filtroLivrosComRetornoPorString =
            listaDeLivros
                    .filter { it.nomeAutor == "Maicon Douglas" }
                    .sortedBy { it.anoPublicacao }
                    .map { it.nomeLivro }
    println(filtroLivrosComRetornoPorString)
    //    A função map irá criar uma lista nova contendo os elementos retornados
    //    pela função ou expressão passada entre as chaves


}

