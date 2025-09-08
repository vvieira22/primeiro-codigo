void main() {
  //Tem um carinha safado chamado tryParse que retorna null se nao conseguir converter
  // em vez de lançar uma exception
  // double? numero = double.tryParse("10.5a");

  // try {
  //   int resultado = 100 ~/ 0;
  //   print(resultado);
  // } on UnsupportedError {
  //   print("UnsupportedError");
  // } catch (e) {
  //   print("Caught an generic exception: $e");
  // } finally {
  //   print("Vai rodar independentemente de ter ou nao exceptions.");
  // }
  try {
    funcao(-10);
  } on MinhaException catch (e) {
    print("Caught MinhaException: $e");
  } catch (e) {
    print("Caught an unexpected exception: $e");
  } finally {
    print("Finalizando o bloco try-catch.");
  }
}

void funcao(int x) {
  if (x < 0) {
    throw MinhaException();
  }
  print("Valor positivo: $x");
}

class MinhaException implements Exception {
  String toString() {
    return "MinhaException: Nao pode passar valor menor que 0.";
  }
}
