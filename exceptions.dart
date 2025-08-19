void main() {
  //Tem um carinha safado chamado tryParse que retorna null se nao conseguir converter
  // em vez de lançar uma exception
  double? numero = double.tryParse("10.5a");

  try {
    int resultado = 100 ~/ 0;
    print(resultado);
  } on UnsupportedError {
    print("UnsupportedError");
  } catch (e) {
    print("Caught an generic exception: $e");
  } finally {
    print("Vai rodar independentemente de ter ou nao exceptions.");
  }
}
