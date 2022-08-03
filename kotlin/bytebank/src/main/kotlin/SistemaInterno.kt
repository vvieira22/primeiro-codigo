class SistemaInterno {

fun entrar(admin: Autenticavel, senha: Int){
    if(admin.autentica(senha)){
        println("Entrou!")
    }
    else{
        println("Senha incorreta!")
    }
}

}