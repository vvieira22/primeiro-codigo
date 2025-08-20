void main() {
  const String nomeFixo = "JOÃO";
  // nomeFixo = nomeFixo; //Variaveis constantes não podem ser alteradas

  //A diferença entre const e final é que final pode ser inicializada em tempo de execução,
  // enquanto const deve ser inicializada em tempo de compilação.
  final String nomeFinal = "JOÃO";
  final DateTime dataAgora =
      DateTime.now(); //isso funciona, mas se usar const nao!
  // nomeFinal = nomeFinal; //Variaveis finais não podem ser alteradas

  //pode ser usado final para variaveis que serão inicializadas depois
  final String sobrenome;
  sobrenome =
      "SILVA"; //final pode ser inicializada depois, mas não pode ser alterada
}
