import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import '../models/tarefa.dart';

//Sempre começa com stateless e ver se precisa mudar para stateful.
class ListaTarefasItem extends StatelessWidget {
  const ListaTarefasItem({super.key, required this.tarefa});

  final Tarefa tarefa;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 8),
      child: Container(
        decoration: BoxDecoration(
          color: Colors.grey[300],
          borderRadius: BorderRadius.circular(5),
        ),
        padding: EdgeInsets.all(8),
        //Container ja tem padding nao precisa colocar widget nele.
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(
              DateFormat('dd/MM/yyyy - HH:mm:ss').format(tarefa.data).toString(),
            ),
            Text(
              tarefa.nomeTarefa,
              style: TextStyle(
                fontSize: 16,
                fontWeight: FontWeight.bold,
              ), //Style do texto
            ),
          ],
        ),
      ),
    );
  }
}
