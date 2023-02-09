public fun testaSetCollections() {
    val assistiramAndroid: MutableSet<String> = mutableSetOf(
        "Vitor", "Manuel", "Pedro"
    )

    val assistiramKotlin: MutableSet<String> = mutableSetOf(
        "Jose", "Vitor", "Maria", "Joao"
    )

    println("Assistiram android e kotlin: ${(assistiramKotlin intersect assistiramAndroid)}")
}
