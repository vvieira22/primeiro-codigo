import 'dart:convert';

void main() {
  String testeJson = """{
    "nome": "Maria",
    "idade": 40,
    "endereço": {
      "rua": "Rua da silva pereira",
      "numero": 101,
      "complemento": "Casa"
    },
    "cursos": [
      {"nome": "C", "dificuldade": 8},
      {"nome": "Python", "dificuldade": 3},
      {"nome": "Kotlin", "dificuldade": 4}
    ]
  }""";

  Map<String, dynamic> dados = json.decode(testeJson);
  print(dados['endereço']);
}
