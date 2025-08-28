import 'dart:ffi';

void main(){
  Pessoa pessoa1 = Pessoa(nome : "João");
  //Posso chamar com construtor especifico
  Pessoa pessoa2 = Pessoa.masculino(nome : "João");
  Pessoa pessoa3 = Pessoa.feminino(nome : "Maria", idade : 20);
  Pessoa? pessoa4;
  print(pessoa4?.idade); //Isso vai printar nulo se pessoa for nulo.
  //isso vale para metodos tambem, nao vai executar se for nulo.
  

  //Em objetos, a referencia acontece, voce aponta onde ta indexado
  //entao se fizer pessoa1 = pessoa2, pessoa2 pode ser alterada e vai refletir em pessoa1.
  //So nao acontece com variaveis primitivas.
  
  pessoa2.idade = 20;  
  
  print(pessoa3);
  print(pessoa3.aniversario());
  print(pessoa3.aniversario());
  pessoa3.dinheiro = 300000.00;
}

class Pessoa { 
  //Construtor
  //Esse é padrao, tem uma safadeza da boa logo embaixo.
  // Pessoa({required String nome}){
  //   this.nome = nome;
  // }
  
  Pessoa({required this.nome}){
    print("Construtor Pessoa xD");
  }
  Pessoa.masculino({required this.nome}){
    print("Construtor Pessoa Masculino xD");
    this.sexo = "Masculino";
  }
  Pessoa.feminino({required this.nome, required this.idade}){
    print("Construtor Pessoa Feminino xD");
    this.sexo = "Feminino";
  }

  String nome;
  int? idade;
  String? sexo;
  
  //colocando _ na frente significa que o atributo é privado.
  double? _dinheiro;
  //criando set and get
  //isso é bom para validar antes de setar ou pegar algo.
  set dinheiro(double? dinheiro){
    print("set dinheiro, modificando dinheiro.");
    _dinheiro = this.dinheiro;
  } 
  double? get dinheiro{
    print("retornando dinheiro");
    return _dinheiro;
  }

  @override
  String toString() => 'Nome: $nome, Idade: $idade, Sexo: $sexo';

  //Metodos
  String aniversario(){
    if(idade != null){
      idade = idade! + 1;
    }
    return "Parabens ${nome}, ele(a) fez ${idade} anos";
  }
}

