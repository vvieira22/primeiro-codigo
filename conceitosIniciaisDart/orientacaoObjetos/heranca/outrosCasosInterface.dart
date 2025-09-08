void main() {
  Movel movel = new Carro(); //Implementa Movel e Vendivel :)
  //Posso ter varias implementacoes de interface em 1 unica classe.
  //respeitando sempre as implementacoes de cada interface.
}

class Geladeira implements Vendivel{
  @override
  double preco() {
    return 1000.0;
  }
}

class Pessoa implements Movel {
  
  String? nome;

  @override
  void direita() {}

  @override
  void esquerda() {}

  @override
  void frente() {}

}

class Carro implements Movel, Vendivel {
  
  String? modelo;

  @override
  void direita() {}

  @override
  void esquerda() {}

  @override
  void frente() {}
  
  @override
  double preco() {
  return 100000.0;
  }
}

abstract class Movel {
  void frente();
  void esquerda();
  void direita();
}

abstract class Vendivel {
  double preco();
}