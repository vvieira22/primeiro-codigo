package br.com.lists

val listaDeLivros: MutableList<Livro> = mutableListOf(
        Livro(
                "Diogo ferreira",
                "Livro 1",
                2021,
                "Coral"
        ),
        Livro(
                "Manuel Gomes",
                "Livro 2",
                2000,
                "Coral"
        ),
        Livro(
                "Vitor Pereira",
                "Livro 3",
                1900,
                "Brasil"
        ),
        Livro(
                "Vitor Pereira",
                "Livro 4",
                2020,
                "Abril"
        ),
        Livro(
                "Vitor Pereira",
                "Livro 5",
                2020,
                "Abril"
        ),
        Livro(
                "Junior da Silva",
                "Livro 6",
                1992,
                "Brasil"
        ),
        Livro(
                "Vitor Manoel",
                "Livro 7",
                2025,
                "Argentina"
        ),
        Livro(
                "Vitor Cley",
                "Livro 8",
                2018,
        )
)

//val listaLivrosComNulos = listaLivros.toMutableList<Livro?>()
val listaLivrosComNulos: MutableList<Livro?> = mutableListOf(
        Livro(
                "Diogo ferreira",
                "Livro 1",
                2021,
                "Coral"
        ),
        Livro(
                "Manuel Gomes",
                "Livro 2",
                2000,
                "Coral"
        ),
        Livro(
                "Vitor Pereira",
                "Livro 3",
                1900,
                "Brasil"
        ),
        Livro(
                "Vitor Pereira",
                "Livro 4",
                2020,
                "Abril"
        ),
        Livro(
                "Vitor Pereira",
                "Livro 5",
                2020,
                "Abril"
        ),
        null,
        Livro(
                "Junior da Silva",
                "Livro 6",
                1992,
                "Brasil"
        ),
        Livro(
                "Vitor Manoel",
                "Livro 7",
                2025,
                "Argentina"
        ),
        Livro(
                "Vitor Cley",
                "Livro 8",
                2018,
        ),
        null,
        null
)

