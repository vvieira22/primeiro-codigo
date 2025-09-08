void main() {
  // For loop: imprime números de 0 a 4
  for (int i = 0; i < 5; i++) {
    print('For loop: $i');
  }

  // While loop: imprime números de 5 a 9
  int j = 5;
  while (j < 10) {
    print('While loop: $j');
    j++;
  }

  // Do-while loop: imprime números de 10 a 14
  int k = 10;
  do {
    print('Do-while loop: $k');
    k++;
  } while (k < 15);

  // For-in loop: itera sobre uma lista
  List<String> nomes = ['Ana', 'Bruno', 'Carlos'];
  for (var nome in nomes) {
    print('For-in loop: $nome');
  }

  // ForEach: usando função anônima
  nomes.forEach((nome) => print('ForEach: $nome'));
}
