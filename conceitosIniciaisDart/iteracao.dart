void main() {
  List<String> nomes = ["Vitor", "Ana", "Carlos", "Beatriz", "João"];

  //Metodo 1
  // for (int i = 0; i < nomes.length; i++) {
  //   print("Nome na posição $i: ${nomes[i]}");
  // }

  //Metodo 2 (mais novo e mais usado)
  for (String nome in nomes) {
    print("Nome: $nome Posicao: ${nomes.indexOf(nome)}");
  }

  //para cada elemento da lista vai fazer operacao dentro
  nomes.forEach((nome) {
    print("Nome: $nome Posicao: ${nomes.indexOf(nome)}");
  });
}
