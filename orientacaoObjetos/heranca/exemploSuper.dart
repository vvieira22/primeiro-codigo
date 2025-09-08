void main() {
  Cachorro cachorro1 = Cachorro(nome:"hammy", idade:10);
  Gato gato1 = Gato(nome:"sherlock", idade:8);

}

class Animal {
  Animal({required this.nome, required this.idade});

  String? nome;
  int? idade;

  void comer(){
    print("comeu class animal");
  }
}

//Dessa forma ele so serve para receber o construtor e passar para o contrutor super no caso animal.
class Gato extends Animal{
  Gato({required nome, required idade}) : super(nome:nome, idade:idade);

  void miar(){
    print("miaaau");
  }
}

class Cachorro extends Animal{
  Cachorro({required super.nome, required super.idade});

  void latir(){
    print("Au au");
  }
}
