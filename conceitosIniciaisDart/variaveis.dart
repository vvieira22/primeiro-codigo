void main() {
  int idade = 25;
  String nome = 'Vitor';
  double altura = 1.80;
  bool estudante = true;

  // Variável opcional/nula
  int? numeroOpcional = 20;
  //pode assumir um valor ou ser nulo se nao for atribuído.
  //mas nao pode ser usado em nenhuma operacao se for atribuído.
  // numeroOpcional = numeroOpcional + 20; (so funciona se definir valor pra ela)

  print(
    'Nome: $nome, '
    'Idade: $idade, '
    'Altura: $altura, '
    'Estudante: $estudante, '
    'Numero Opcional: $numeroOpcional',
  );
}
