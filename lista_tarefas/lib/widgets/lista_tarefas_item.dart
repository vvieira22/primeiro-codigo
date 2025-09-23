import 'package:flutter/material.dart';
import 'package:flutter_slidable/flutter_slidable.dart';
import 'package:intl/intl.dart';

import '../models/tarefa.dart';

//Sempre começa com stateless e ver se precisa mudar para stateful.
class ListaTarefasItem extends StatelessWidget {
  const ListaTarefasItem({super.key, required this.tarefa, required this.onDelete});

  final Tarefa tarefa;
  final Function(Tarefa) onDelete;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4),
      child: Slidable(
        endActionPane: ActionPane(
          motion: const DrawerMotion(),
          extentRatio: 0.5,
          children: [
            SlidableAction(
              label: 'Editar',
              backgroundColor: Colors.blue,
              icon: Icons.edit,
              onPressed: (context) {},
            ),
            SlidableAction(
              label: 'Excluir',
              backgroundColor: Colors.red,
              icon: Icons.delete,
              onPressed: (context) {
                onDelete(tarefa);
              },
            ),
          ],
        ),
        child: Padding(
          padding: const EdgeInsets.symmetric(vertical: 0),
          child: Container(
            decoration: BoxDecoration(
              color: Colors.grey[300],
              borderRadius: BorderRadius.circular(5),
            ),
            padding: EdgeInsets.all(16),
            //Container ja tem padding nao precisa colocar widget nele.
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                Text(
                  DateFormat(
                    'dd/MM/yyyy - HH:mm:ss',
                  ).format(tarefa.data).toString(),
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
        ),
      ),
    );
  }
}
