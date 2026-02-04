import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_svg/flutter_svg.dart';
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
                      SizedBox(
                        height: 16,
                      ),
                      TextField(
                        controller: _emailControler,
                        style: defaultInputTextSyle,
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
                        style: defaultInputTextSyle,
                        decoration: buildDarkInputDecoration(
                          label: "Senha",
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
                            _buildSocialIcon(context, 'assets/icons/facebook_icon.svg', 'Facebook'),
                            SizedBox(width: 24),
                            _buildSocialIcon(context, 'assets/icons/gmail_icon.svg', 'Google'),
                            SizedBox(width: 24),
                            _buildSocialIcon(context, 'assets/icons/x_icon.svg', 'X (Twitter)'),
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

  // Método auxiliar para padronizar o tamanho e clique dos ícones
  Widget _buildSocialIcon(BuildContext context, String assetPath, String socialName) {
    return GestureDetector(
      onTap: () {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text("Login com $socialName"),
            duration: const Duration(seconds: 2),
            behavior: SnackBarBehavior.floating,
          ),
        );
      },
      child: SizedBox(
        width: 32,
        height: 32,
        child: SvgPicture.asset(
          assetPath,
          fit: BoxFit.contain,
        ),
      ),
    );
  }
}
