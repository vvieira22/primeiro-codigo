package br.com.codigosIniciais

import java.math.BigDecimal

fun Array<BigDecimal>.somatoria(): BigDecimal {
/*
     Acumula valor da string, com primeiro elemento e faz uma operação para agregar os outros
    no caso abaixo vai fazer a soma de todos elementos, como se fosse um for somando primeiro
    com o segunto, até o último elementro do array.
 */

    return this.reduce { acumulador, valor ->
        acumulador + valor
    }
}

fun Array<BigDecimal>.media(): BigDecimal {
    return if(this.isEmpty()){
        BigDecimal.ZERO
    }else{
        this.somatoria() / this.size.toBigDecimal()
    }
}