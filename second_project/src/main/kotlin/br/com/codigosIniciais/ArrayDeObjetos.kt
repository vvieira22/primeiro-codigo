package br.com.codigosIniciais

import java.math.BigDecimal
import java.math.RoundingMode

fun main() {

//double faz aproximações, para números exatos melhor trabalhar com BigDecimal
//    var salarios = Array<BigDecimal>(5) { BigDecimal.ZERO }

//é melhor jogar o valor para string e converter para bigDecimal
//por causa do double entre outros terem problemas de arrendondamento.
//    salarios[0] = "1500.55".toBigDecimal()
//    salarios[1] = "12200.55".toBigDecimal()
//    salarios[2] = "00.55".toBigDecimal()
//    salarios[3] = "500.433333".toBigDecimal()
//    salarios[4] = "1.55".toBigDecimal()

//println(salarios.contentToString())

//Ao envez de ficar linha pro linha
//vamos usar a função que criamos bigDecimalArrayOf para facilitar
    var salarios = bigDecimalArrayOf("1000.00", "1000", "3000", "12029.887", "50000", "78222.88")
    println(salarios.contentToString())

    //aumento proporcional
    val salariosComAumento: Array<BigDecimal>  = aumentarSalarios(salarios)
    println(salariosComAumento.contentToString())

    val somaSalariosAtualizada =  salariosComAumento.somatoria()
    println("Gasto 1 mes reajustado $somaSalariosAtualizada")

    //Calcular aumento para próximos meses
    val meses = 6.toBigDecimal()
    val gasto6meses = salariosComAumento.fold(somaSalariosAtualizada) { acumulador, salario ->
        acumulador + (salario * meses).setScale(2, RoundingMode.UP)
    }
    println("Gasto em 6 meses: $gasto6meses")

    /*
    Precisamos descobrir os 3 maiores salários depois do aumentos
    primeiro ordenar do maior pro maior e dps pegar os 3 últimos
    sorted retorna lista menor para maior
    */
//    val salariosOrdenados = salariosComAumento.sorted()
//    val tresMaioresSalarios: Array<BigDecimal> = salariosOrdenados.takeLast(3)
//            .toTypedArray()
//    val media = tresMaioresSalarios.media()
//    println("Media tres maiores salarios:  $media")
    /*
    Uma forma de fazer isso tudo anteriormente mais efetivo:

     */
    var media: BigDecimal = salariosComAumento
            .sorted().
            takeLast(3).
            toTypedArray().
            media()
    println("Media tres maiores salarios:  $media")
}

//vararg são argumentos variados, 1,2,3 etc...
fun bigDecimalArrayOf(vararg valores: String): Array<BigDecimal> {

    //o i o proprio construtor do kotlin cria pra gente navegar
    return Array<BigDecimal>(valores.size) { i ->
        valores[i].toBigDecimal()
    }
}

fun aumentarSalarios(salarios: Array<BigDecimal>): Array<BigDecimal> {
/*
     Todos funcionarios aumento de 5%
    Acima de 3000 = 10% aumento
 */

    val aumentoPadrao = "1.05".toBigDecimal()
    val aumentoAcimaPadrao = "1.1".toBigDecimal()

    val salarioComAumento: Array<BigDecimal> = salarios
            .map { salario -> calculaAumentoRelativo(salario, aumentoAcimaPadrao, aumentoPadrao) }
            .toTypedArray()
//setScale é pra limitar casas decimais,com arrendondamento pra cima.

    return salarioComAumento
}

private fun calculaAumentoRelativo(salario: BigDecimal, aumentoAcimaPadrao: BigDecimal, aumentoPadrao: BigDecimal): BigDecimal {
    return if (salario >= "3000.00".toBigDecimal()) {
        salario * aumentoAcimaPadrao.setScale(2, RoundingMode.UP)
    } else {
        salario * aumentoPadrao.setScale(2, RoundingMode.UP)
    }
}


