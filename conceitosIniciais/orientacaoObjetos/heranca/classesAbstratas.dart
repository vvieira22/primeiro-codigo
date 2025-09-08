void main() {
  Cachorro cachorro1 = Cachorro(nome:"hammy", idade:10);
  Gato gato1 = Gato(nome:"sherlock", idade:8);

  //Dessa forma eu consigo criar animal separado, as vezes em alguns cenários a gente nao quer ser capaz
  //de instanciar essa super classse diretamente, so usar especifico, nao quero generico!!
  //colocando ABSTRACT, nao consigo mais criar Animal.
}

abstract class Animal {
  Animal({required this.nome, required this.idade});

  String? nome;
  int? idade;

  void comer(){
    print("comeu class animal");
  }

  void morder(); //Esse metodo dessa forma precisa ser implementado por todos que extendem!
}

class Gato extends Animal{
  Gato({required super.nome, required super.idade});

  void miar(){
    print("miaaau");
  }
  void morder(){print("gato mordeu.");}
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

  void morder(){print("cachorro mordeu.");}
}
