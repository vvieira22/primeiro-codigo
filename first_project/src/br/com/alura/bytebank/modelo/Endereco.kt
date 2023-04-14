package br.com.alura.bytebank.modelo

class Endereco (
    var logradouro: String = "",
    var numero: Int = 99999999,
    var bairro: String = "" ,
    var cidade: String = "",
    var estado: String = "",
    var cep: String = "",
    var complemento: String = ""
)
{
    override fun toString(): String {
        return  "Logradoro:   $logradouro\n" +
                "Numero:      $numero\n" +
                "Bairro:      $bairro\n" +
                "Cidade:      $cidade\n" +
                "Estado:      $estado\n" +
                "Cep:         $cep\n" +
                "Complemento: $complemento"
    }

    fun enderecoCompleto() : String{
        return """ 
            $logradouro - $numero - $bairro - $cidade - $estado
            $cep
            $complemento
        """.trimIndent()
    }
}
