main() {
  var notas = [1, 5, 10, 7.3, 9.8, 3.1]; // Lista de notas

  // Assim define lista que so aceita 1 tipo so, de cima é como se fosse de baixo so que dynamic.
  List<int> listaNotasDefinidas = [1, 5, 10, 8, 10];

  // lista que pode aceitar null ou o tipo dela mesmo, importante.
  List<String?> listaQueAceitaNull = [null, "Vitor"];
  print(listaQueAceitaNull);

  //Permite que a lista seja inicializada com nula!
  List<String>? listaQueComecaComNull;
  print(listaQueComecaComNull);

  //Permite que a lista seja inicializada com nula e tenha elementos nulos!
  List<String?>? listaQueComecaComNullEtEMnULL;
  print(listaQueComecaComNull);

  for (var nota in notas) {
    print("A nota é: $nota");
  }

  var nomes = ["Ana", "Bia", "Carlos", "Daniel", "Maria"]; // Lista de nomes
  nomes.add("Ricardo");
  print(nomes.length);
  print(nomes.elementAt(0));
  print(nomes.removeAt(0)); //remove pelo indice
  print(nomes.remove(0)); //remove a primeira ocorrencia do valor
  nomes.shuffle(); //embaralha a lista
  nomes.clear(); //limpa a lista
  print(nomes);
  // print(nomes[0]);
  print(nomes);

  var frutas = ["morango", "uva", "abacaxi"];
  frutas.add("melancia");
  print(frutas);

  // Declarando um conjunto (Set) - não aceita elementos duplicados
  var conjunto = {0, 1, 2, 3, 4, 5, 5, 6, 7, 7};
  print(conjunto.length);
  print(conjunto is Set);
  print(conjunto.contains(1));


}
