//Static significa que os metodos e atributos nao sejam mais pertencentes ao objeto mas asim a classe.
void main(){
  Pessoa pessoa1 = Pessoa(nome: "João", idade: 20);
  pessoa1.cpf = "1021021021";
  print(pessoa1.cpf);
  print(pessoa1.temperatura); //so vai chamar o metodo medirTemperatura se eu chamar a variavel..  lateinit.
}

class Pessoa {
  Pessoa({required this.nome, required this.idade});
  String nome;
  int idade;
  late String cpf; //usar late se, nao faz sentido ter valor nulo em uma variavel e vou preencher depois..
  late double temperatura = medirTemperatura(); //so preciso ter quando realmente eu precisar, pq sao dados chatos e dificies..
  
  double medirTemperatura(){
    return 36.9;
  }
}