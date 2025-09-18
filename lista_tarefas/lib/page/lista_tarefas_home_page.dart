import 'package:flutter/material.dart';
import 'package:lista_tarefas/widgets/lista_tarefas_item.dart';

import '../models/tarefa.dart';

class TodoListHomePage extends StatefulWidget {
  TodoListHomePage({super.key});

  @override
  State<TodoListHomePage> createState() => _TodoListHomePageState();
}

class _TodoListHomePageState extends State<TodoListHomePage> {
  final TextEditingController campoTarefa = TextEditingController();

  List<Tarefa> tarefas = [];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Padding(
          padding: const EdgeInsets.fromLTRB(24,122,24,122),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            //ISSO DIZ QUE A COLUNA VAI TER SO O TAMANHO DOS ELEMENTOS!
            children: [
              Row(
                children: [
                  //se eu quiser colocar elementos com mesmo tamanho posso usar 2 expanded pra dividir.
                  Expanded(
                    // flex:2, //valores relativos de acordo com Expanded da regiao.
                    child: TextField(
                      controller: campoTarefa,
                      decoration: InputDecoration(
                        hintText: 'Ex. Estudar Python.',
                        labelText: 'Tarefa',
                        labelStyle: const TextStyle(
                          fontSize: 25,
                          color: Colors.black,
                        ),
                        // prefixText: 'R\$ '
                        // suffixText: 'Texto fixo na direita',
                        border: OutlineInputBorder(),
                      ),
                      style: const TextStyle(fontSize: 20, color: Colors.black),
                      keyboardType: TextInputType.emailAddress,
                      // obscureText: true, this is for passwords.
                    ),
                  ),
                  SizedBox(width: 10),
                  ElevatedButton(
                    onPressed: addTarefa,
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.lightBlue,
                      foregroundColor: Colors.white,
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(10),
                      ),
                      padding: EdgeInsets.all(16),
                    ),
                    child: Icon(Icons.add, size: 30, color: Colors.white),
                  ),
                ],
              ),
              SizedBox(height: 16),
              Flexible( //Flexible limita os componentes ao maximo possivel sem quebrar layout. e força scroll junto com o shrinkWrap.
                child: ListView(
                  shrinkWrap: true,
                  //aumenta tamanho baseado no espaço disponivel.
                  children: [
                    for(Tarefa tarefa in tarefas)
                      ListaTarefasItem(
                          tarefa: tarefa
                      ),
                  ],
                ),
              ),
              SizedBox(height: 16),
              Row(
                children: [
                  Expanded(child: Text('Você possui ${tarefas.length} tarefas pendentes.')),
                  ElevatedButton(
                    onPressed: null,
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.red,
                      foregroundColor: Colors.white,
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(10),
                      ),
                      padding: EdgeInsets.all(14),
                    ),
                    child: Text('Limpar Tarefas'),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }

  void addTarefa() {
    Tarefa novaTarefa = Tarefa(
      nomeTarefa: campoTarefa.text,
      data: DateTime.now(),
    );
    setState(() {
      tarefas.add(novaTarefa);
    });
  }

  void onChanged(String text) {
    print(text);
  }

  //Sempre que eu digitar texto e apertar "enter/ok do android ".
  void onSubmitted(String text) {
    print(text);
  }
}
