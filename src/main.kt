import src.br.com.alura.bytebank.modelo.Teste

fun main() {
//    a classe abstrata serve como base
//    para a gente representar
//    apenas, como por exemplo funcionario
//    não existe cargo funcionario, existe analista etc..
//    so servir como base, nao pode ser usado.
//    Abstract já é classe aberta
//ao criar um mebro abstrado é necessário que os filhos
    //tenham esse método implementado.
//Interface é abstrata
    //interface nao mantem valor das variaveis(status)
    //construtor nao existe em interface.
    //interface nao vai ter o vinculo todo igual herença
    // interface = contrato, quem usa tem que implementar.

    println("função main");
    funcao1();
    println("fim main");
}

fun funcao1(){
    println("inicio funcao 1");
    funcao2();
    println("fim funcao 1");
}
fun funcao2(){
    println("inicio funcao 2");
    for (i in 1..5){
        println(i);
    }
    var a: Int
    var b: String
    b = "akaska"

    try {
        a = b.toInt();
    }
    catch (e: NumberFormatException){
        println("erro ao converter: ");
        e.printStackTrace()
    }

    println("fim funcao 2");
}






