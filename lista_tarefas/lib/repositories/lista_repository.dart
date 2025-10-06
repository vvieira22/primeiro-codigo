import 'dart:convert';

import 'package:shared_preferences/shared_preferences.dart';

import '../models/tarefa.dart';

const listaTarefasKey = 'lista_tarefas';

class ListaRepository {
  //Garanto que vou em algum momento preencher ela!
  late SharedPreferences sharedPreferences;

  Future<List<Tarefa>> getListas() async{
    sharedPreferences = await SharedPreferences.getInstance();
    final String jsonString = sharedPreferences.getString(listaTarefasKey) ?? '[]';
    final List<dynamic> jsonDecoded = json.decode(jsonString);
    return jsonDecoded.map((e) => Tarefa.fromJson(e)).toList();
  }

  // Internamente, `json.encode()` verifica se os objetos na lista possuem
  // um método `toJson()`. Se possuírem, ele chama esse método para cada objeto.
  void saveTodoList(List<Tarefa> tarefas){
    final jsonString = json.encode(tarefas);
    sharedPreferences.setString(listaTarefasKey, jsonString);
  }
}