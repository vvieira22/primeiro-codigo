// widgets/custom_drawer.dart
import 'package:flutter/material.dart';
import 'package:silk_deaths/theme/app_colors.dart';

class HomeDrawer extends StatelessWidget {
  const HomeDrawer({super.key});

  // Função para fechar o Drawer antes de navegar
  void _closeDrawer(BuildContext context) {
    Navigator.of(context).pop();
  }

  @override
  Widget build(BuildContext context) {
    return Drawer(
      backgroundColor: AppColors.backgroundElementsColor,
      child: ListView(
        // Remova qualquer padding do ListView.
        padding: EdgeInsets.zero,
        children: <Widget>[
          // 1. Cabeçalho do Drawer (Opcional, mas comum)
          const DrawerHeader(
            child: Text(
              'Menu Principal',
              style: TextStyle(
                color: Colors.white,
                fontSize: 30,
              ),
            ),
          ),

          // 2. Item de Navegação 1: Home
          ListTile(
            leading: const Icon(Icons.home),
            title: const Text('Início'),
            onTap: () {
              // Fecha o drawer
              _closeDrawer(context);
              // Exemplo de navegação para a própria Home
              // Em um app real, você pode substituir a tela atual
              // Navigator.of(context).pushReplacementNamed('/home');
            },
          ),

          // 3. Item de Navegação 2: Configurações
          ListTile(
            leading: const Icon(Icons.settings),
            title: const Text('Configurações'),
            onTap: () {
              _closeDrawer(context);
              // Lógica de navegação para a tela de configurações
              // Navigator.of(context).pushNamed('/settings');
            },
          ),

          const Divider(), // Linha divisória

          // 4. Item de Ação
          ListTile(
            leading: const Icon(Icons.exit_to_app),
            title: const Text('Logout'),
            onTap: () {
              _closeDrawer(context);
              // Lógica para deslogar o usuário
              // print('Usuário deslogado');
            },
          ),
        ],
      ),
    );
  }
}