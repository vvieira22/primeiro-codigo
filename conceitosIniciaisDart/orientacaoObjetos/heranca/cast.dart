void main() {
  Cachorro cachorro1 = Cachorro(nome:"hammy", idade:10);
  Gato gato1 = Gato(nome:"sherlock", idade:8);
 
 //A operacao de cast consiste em saber o retorno de alguem e ter certeza que é o retorno.
 //No caso espera que o gato seja recebido por causa do as Gato, mas se der ruim...
  Animal gatoCast = funcao() as Gato;
  //Se nao retornar gato, vai dar erro e gerar exception.
  //Cachorro is not a subtype of Gato, ou seja, subtipo é uma classe que extende o supertipo.
  //Bom colocar isso em um try catch ou tirar o as e verificar com if qual tipo.
}

Animal funcao(){
  return Gato(nome:"sherlock", idade:8);
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
