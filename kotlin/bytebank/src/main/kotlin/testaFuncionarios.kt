fun testarFuncionarios() {
    val vitor = Diretor(
        nome = "vitor",
        cpf = "12256122765",
        salario = 4000.0,
        senha = 123,
        plr = 10.0
    )
    val maicon = Gerente(
        nome = "vitor",
        cpf = "12256122765",
        salario = 1000.0,
        senha = 12354
    )
    val maria = Analista(
        nome = "maria",
        cpf = "121012012",
        salario = 3000.0
    )

    val calcBonus = CalculadoraBonificacao()
    calcBonus.registra(maicon)
    calcBonus.registra(vitor)
    calcBonus.registra(maria)

    println("bonus total: ${calcBonus.total}")

    if(maicon.autentica(12354)){
        println("autenticado")
    }
    else{
        println("não autenticado")
    }

}