package br.com.codigosIniciais

fun Ranges (){

//inclusiva, vai ate o 100
//0-100
val rangeNumeros = 0..100 step 1

//da pra tirar o ultimo usando isso:
//0-99
//val rangeNumeros = 0.until(100) step 1

//inverter lista
// val numerosReversos = 100 downto 0 step 1

for(numero in rangeNumeros){
    print("$numero ");
}

//intervalo de valores
val intervalo = 5000.0..10000.0
val salario = 6000.0

if(salario in intervalo){
    println("")
    println("salario dentro do invervalo!!!")
}

val alfabeto = 'a'..'z'
val letra = 'k'
printLn(letra in alfabeto)

}