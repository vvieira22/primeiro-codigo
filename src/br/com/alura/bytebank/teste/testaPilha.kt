package src.br.com.alura.bytebank.teste

import src.br.com.alura.bytebank.exception.SaldoInsuficienteException

fun funcao1(){
    println("inicio funcao 1");

    try{
        funcao2();
    }
    catch (e: SaldoInsuficienteException){
        println("erro ao converter: ");
        e.printStackTrace()
    }
    println("fim funcao 1");
}

fun funcao2(){
    println("inicio funcao 2");
    for (i in 1..5){
        println(i);
    }
    var a: String
    var b: String
    b = "akaska"

    a = b

    throw SaldoInsuficienteException();
    println("fim funcao 2");
}
