void main() {
  Cachorro cachorro1 = Cachorro(nome:"hammy", idade:10);
  Gato gato1 = Gato(nome:"sherlock", idade:8);
  gato1.miar();
  cachorro1.latir();
  cachorro1.comer();

  //Se eu quero uma lista com gato e cachorro, simplesmente posso criar uma lista de Animal
  List<Animal> listaAnimais = [];
  listaAnimais.add(cachorro1);
  listaAnimais.add(gato1);

  //Mas o dart ainda acha que cachorro1 e gato1 sao animal, nao vai ter as coisas
  //especificas de cada classe. A melhor alternativa
  var primeiroElemento = listaAnimais.first;
  if(primeiroElemento is Cachorro){
    print("É um cachorro");
    primeiroElemento.latir();
  }else if(primeiroElemento is Gato){
    print("É um gato");
    primeiroElemento.miar();
  }
  //A mesma coisa acontece quando uma funcao pode retornar gato ou cachorro
  //retorna logo a classe que extende as duas =) e trata.
}


class Animal {
  //Se isso aqui é requerido, entao quem herda ela tambem precisa declarar.
  Animal({required this.nome, required this.idade});

  String? nome;
  int? idade;

  void comer(){
    print("comeu class animal");
  }
}

class Gato extends Animal{
  Gato({required super.nome, required super.idade});

  void miar(){
    print("miaaau");
  }
}

class Cachorro extends Animal{
  Cachorro({required super.nome, required super.idade});

  void latir(){
    print("Au au");
  }
 
  @override
  void comer(){
    super.comer();
    print("Cachorro comeu.");
  }
}
