void main() {
  int idade = 20;

  // if-else
  if (idade >= 18) {
    print('Maior de idade');
  } else {
    print('Menor de idade');
  }

  // if-else if-else
  double nota = 7.5;
  if (nota >= 9) {
    print('Excelente');
  } else if (nota >= 7) {
    print('Bom');
  } else {
    print('Precisa melhorar');
  }

  // switch-case
  String dia = 'segunda';
  switch (dia) {
    case 'segunda':
      print('Início da semana');
      break;
    case 'sexta':
      print('Fim de semana chegando');
      break;
    default:
      print('Dia comum');
  }

  // Operador ternário
  bool aprovado = nota >= 7 ? true : false;
  print(aprovado ? 'Aprovado' : 'Reprovado');
}
