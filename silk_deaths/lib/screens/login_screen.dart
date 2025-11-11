import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:silk_deaths/screens/register_screen.dart';

import '../theme/app_colors.dart';
import '../theme/app_textfield_style.dart';


class LoginScreen extends StatelessWidget {
  const LoginScreen({super.key});

  TextEditingController? get _emailControler => null;
  TextEditingController? get _passwordControler => null;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomInset: false,
      body: Container(
        padding: EdgeInsets.all(20),
        color: Colors.black, // Cor de fundo da tela
        child: Center(
          //Tem que usar esse cara pois permite que o usuario de scroll pra ver enquanto ta com teclado aberto.
          child: SingleChildScrollView(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Container(
                  padding: EdgeInsets.fromLTRB(16,16,16,8),
                  decoration: BoxDecoration(
                    color: AppColors.backgroundElementsColor,
                    borderRadius: BorderRadius.circular(16),
                  ),
                  child: Column(
                    children: [
                      Image.asset(
                        'assets/images/silk_deaths_logo.png', // Caminho para a sua imagem
                        width: 340,
                        height: 150,
                      ),
                      // Image.asset(
                      //   'assets/images/icon_launcher.png', // Caminho para a sua imagem
                      //   width: 124,
                      //   height: 124,
                      // ),
                      SizedBox(
                        height: 16,
                      ),
                      TextField(
                        controller: _emailControler,
                        decoration: buildDarkInputDecoration(
                          label: "Email",
                        ),
                      ),
                      SizedBox(
                        height: 16,
                      ),
                      TextField(
                        obscureText: true,
                        controller: _passwordControler,
                        decoration: InputDecoration(
                          labelText: "Senha",
                          border: OutlineInputBorder(),
                        ),
                      ),
                      SizedBox(
                        height: 20,
                      ),
                      ElevatedButton(
                        onPressed: () {},
                        style: ElevatedButton.styleFrom(
                          padding: EdgeInsets.symmetric(horizontal: 42, vertical: 12),
                        ),
                        child: Text("Entrar"),
                      ),
                      SizedBox(
                        height: 16,
                      ),
                      Center(
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            FlutterLogo(
                              size: 36,
                            ),
                            SizedBox(
                              width: 10,
                            ),
                            FlutterLogo(
                              size: 36,
                            ),
                            SizedBox(
                              width: 10,
                            ),
                            FlutterLogo(
                              size: 36,
                            ),
                          ],
                        ),
                      ),
                      TextButton(
                        onPressed: () {},
                        child: Text("Esqueceu a senha?"),
                      ),
                      TextButton(
                        onPressed: () {
                          Navigator.push(
                            context,
                            MaterialPageRoute(builder: (context) => RegisterScreen()),
                          );
                        },
                        child: Text("Primeiro acesso? Crie uma conta aqui"),
                      ),
                    ],
                  )
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

