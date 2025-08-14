// ignore_for_file: dead_code
// rs,isso é legal, ignorar código morto ou inacessivel no topo do arquivo.
void main() {
  // Operadores Aritméticos
  int a = 10;
  int b = 5;

  print("Soma: ${a + b}");
  print("Subtração: ${a - b}");
  print("Multiplicação: ${a * b}");
  print("Divisão: ${a / b}");
  print("Módulo: ${a % b}");

  // Operadores de Atribuição
  int c = 20;
  c += 5; // c = c + 5
  print("Atribuição com soma: $c");

  // Operadores de Comparação
  print("Igualdade: ${a == b}");
  print("Desigualdade: ${a != b}");
  print("Maior que: ${a > b}");
  print("Menor que: ${a < b}");

  // Operadores Lógicos
  bool x = true;
  bool y = false;

  print("AND lógico: ${x && y}");
  print("OR lógico: ${x || y}");
}
