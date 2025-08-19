void main() {
  List<String> nomes = List.filled(10, "Vitor");
  print(nomes);

  List<int> lista = List.generate(10, (int valor) {
    return valor * 2;
  });
  //podemos ainda colocar assim bonitinho
  List<int> lista2 = List.generate(10, (valor) => (valor + 1));
  print(lista2);

  print(lista2.isEmpty);
  print(lista2.isNotEmpty);

  //verifica se existe algum elemento que atenda a condicao
  print(lista2.any((i) => i > 1));

  //retorna primeiro elemento que atendem a condicao
  print(lista2.firstWhere((i) => i % 2 == 0));
  //retorna ultimo elemento que atende a condicao
  print(lista2.lastWhere((i) => i % 2 == 0));
  //retorna todos resultados que atendem a condicao
  print(lista2.where((i) => i % 2 == 0));

  //map, para cada elemento da lista, aplica uma funcao e retorna uma nova lista
  //vai retorna uma nova lista, onde cada elemento da anterior foi incrementado em 1
  print(lista2.map((i) => i + 1));
  //Lembrando, voce pode abrir em uma funcao complexa
  //para fazer mais coisa. tipo isso aqui
  print(
    lista2.map((i) {
      if (i % 2 == 0) {
        return i + 1;
      } else {
        return i;
      }
    }),
  );
}
