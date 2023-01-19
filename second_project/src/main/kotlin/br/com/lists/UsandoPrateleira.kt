package br.com.lists

fun main() {
    val prateleiraAcao = Prateleira(
            genero = "Literatura",
            livros = listaDeLivros
    )

    val porAno = prateleiraAcao.organizarPorAno()
    val porAutor = prateleiraAcao.organizarPorAutor()

    porAno.imprimeComMarcadores()
    println("Lista Por Ano: ${porAno.hashCode()}")

    porAutor.imprimeComMarcadores()
    println("Lista Por Autor: ${porAutor.hashCode()}")

    /*Hashcode para mostrar que lista != mutablelist
    isso garante que cada execucao vai criar um objeto diferente no retorno
     e nao alterar o original criado (mutablelist). */
}