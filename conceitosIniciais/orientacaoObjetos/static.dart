//Static significa que os metodos e atributos nao sejam mais pertencentes ao objeto mas asim a classe.
void main(){
  //Definindo atributos estaticos posso definir para aquela classe naquele cenario certos comportamentos..
  //tipo definir altura padrao para o objeto antes de instanciar alguem do tipo dele.
  Pessoa.alturaPadrao = 1.80;
  //TODAS AS PESSOAS NESSE CONTEXTO TEM A MESMA ALTURA PADRÃO.
  Pessoa pessoa1 = Pessoa(nome: "João", idade: 20);
  print(pessoa1.altura); //nao passei altura logo vai ser 1.80
  // pessoa1.atributoStatic
  Pessoa.atributoStatic = "Valor";
  print(Pessoa.atributoStatic);
}

class Pessoa {
  Pessoa({required this.nome, required this.idade});
  String nome;
  int idade;
  double altura = alturaPadrao;

  static String atributoStatic = "";
  static double alturaPadrao = 0;
  
}