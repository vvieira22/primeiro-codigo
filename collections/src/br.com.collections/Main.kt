fun main() {
    val usuarios = mapOf<String, Long>(
    "Maicon" to 52256334237,
    "Vitor" to 32256331237,
    "Mariana" to 92256993237)

    println(usuarios)

    for(par in usuarios)
    {
        print("${par.key}: ")
        println(par.value)
    }

    //Tentando achar um valor para uma chave
    usuarios[""]?.let{
        println("Achou a pessoa: $it")
    }

    //Comportamento de escrita
    val usuarios2 : MutableMap<String, Long> = mutableMapOf(
        "Maicon" to 52256334237,
        "Vitor" to 32256331237,
        "Mariana" to 92256993237)

    usuarios2["Joao"] = 922569522563
    //ou
    usuarios2.put("Joao", 922569522563)

    //Adicionar se ele realmente nao existir
    usuarios2.putIfAbsent("Joao", 922569522563)

    //Remocao
    usuarios2.remove("Joao")
    //ou
    //aqui gera sobrecarga, ambos precisam estar certo pra remover.
    usuarios2.remove("Joao", 922569522563)

    println(usuarios2)

}


