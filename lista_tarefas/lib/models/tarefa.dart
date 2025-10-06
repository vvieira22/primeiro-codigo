import 'dart:convert';

class Tarefa {
  Tarefa({required this.nomeTarefa, required this.data});

  Tarefa.fromJson(Map<String, dynamic> json)
  : nomeTarefa = json['nomeTarefa'],
    data = DateTime.parse(json['data']);

  String nomeTarefa;
  DateTime data;

  // Internamente, `json.encode()` verifica se os objetos na lista possuem
  // um método `toJson()`. Se possuírem, ele chama esse método para cada objeto.
  Map<String, dynamic> toJson(){
    return {
      'nomeTarefa': nomeTarefa,
      'data': data.toIso8601String(),
    };
  }
}
