void main() {
  saudacao();
  int resultado = soma(5, 3);
  print('A soma de 5 e 3 é $resultado');
  print('O dobro de 10 é ${dobro(10)}');
  mostrarMensagem('Olá', idade: 25, nome: 'Vitor');
  exemplo('A'); // A, B, C
  exemplo('A', 'X'); // A, X, C
}

// Função sem retorno e sem parâmetros
saudacao() {
  print('Olá, bem-vindo ao exemplo de funções em Dart!');
}

// Função com parâmetros e retorno
int soma(int a, int b) {
  return a + b;
}

// Função com expressão curta (arrow function)
int dobro(int numero) => numero * 2;

// Função com parâmetro padrão posicional ( preciso especificar o nome do parâmetro)
void mostrarMensagem(
  String mensagem, {
  String nome = 'usuário',
  required int idade,
}) {
  print('$mensagem, $nome!, você tem $idade anos.');
}

// Função com parâmetros opcionais nomeados
void exemplo(String a, [String b = 'B', String c = 'C']) {
  print('$a, $b, $c');
}

// Função que recebe outra função como parâmetro
void executarOperacao(int x, int y, int Function(int, int) operacao) {
  int resultado = operacao(x, y);
  print('Resultado da operação: $resultado');
}

// Exemplo de uso:
void exemploFuncaoParametro() {
  executarOperacao(4, 2, soma); // Usando a função soma definida acima
  executarOperacao(
    6,
    3,
    (a, b) => a * b,
  ); // Usando uma função anônima (multiplicação)
}
