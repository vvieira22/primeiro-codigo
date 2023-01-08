package br.com.codigosIniciais

import java.math.BigDecimal
import java.math.RoundingMode

fun main() {

//double faz aproximações, para números exatos melhor trabalhar com BigDecimal
var salarios = Array<BigDecimal>(5) { BigDecimal.ZERO }

//é melhor jogar o valor para string e converter para bigDecimal
//por causa do double entre outros terem problemas de arrendondamento.
salarios[0]="1500.55".toBigDecimal()
salarios[1]="12200.55".toBigDecimal()
salarios[2]="00.55".toBigDecimal()
salarios[3]="500.433333".toBigDecimal()
salarios[4]="1.55".toBigDecimal()

//println(salarios.contentToString())


//Ao envez de ficar linha pro linha
//vamos usar a função que criamos bigDecimalArrayOf para facilitar

salarios = bigDecimalArrayOf("1000.00","10000.40", "3000")
println(salarios.contentToString())

println(aumentarSalarios(salarios).contentToString())

}

//vararg são argumentos variados, 1,2,3 etc...
fun bigDecimalArrayOf(vararg valores: String) : Array<BigDecimal> {

    //o i o proprio construtor do kotlin cria pra gente navegar
    return Array<BigDecimal>(valores.size) { i ->
        valores[i].toBigDecimal()
    }

}

fun aumentarSalarios(salarios : Array<BigDecimal>) : Array<BigDecimal> {
//Todos funcionarios aumento de 5%
//Acima de 3000 = 10% aumento

val aumentoPadrao = "1.05".toBigDecimal()
val aumentoAcimaPadrao = "1.1".toBigDecimal()

    val salarioComAumento: Array<BigDecimal> = salarios.
    map { salario ->
        if(salario >= "3000.00".toBigDecimal()){
            salario * aumentoAcimaPadrao.setScale(2, RoundingMode.UP)
        }
        else{
            salario * aumentoPadrao.setScale(2, RoundingMode.UP)
        }
    }.toTypedArray()

//Todos funcionarios aumento de 5%
//setScale é pra limitar casas decimais. arrendondando pra cima.
return salarioComAumento
}