import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_svg/flutter_svg.dart';
import 'package:provider/provider.dart';
import 'package:silk_deaths/screens/register_screen.dart';

import '../theme/app_colors.dart';
import '../theme/app_textfield_style.dart';
import '../viewmodels/auth_view_model.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  // Inicializando os controladores corretamente
  final TextEditingController _emailController = TextEditingController(text: "vitor123@gmail.com");
  final TextEditingController _passwordController = TextEditingController(text: "123456");

  @override
  void dispose() {
    // É importante dar dispose nos controladores ao sair da tela
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomInset: false,
      body: Container(
        padding: const EdgeInsets.all(20),
        color: Colors.black,
        child: Center(
          child: SingleChildScrollView(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Container(
                  padding: const EdgeInsets.fromLTRB(16, 16, 16, 8),
                  decoration: BoxDecoration(
                    color: AppColors.backgroundElementsColor,
                    borderRadius: BorderRadius.circular(16),
                  ),
                  child: Column(
                    children: [
                      Image.asset(
                        'assets/images/silk_deaths_logo.png',
                        width: 340,
                        height: 150,
                      ),
                      const SizedBox(height: 16),
                      TextField(
                        controller: _emailController,
                        style: defaultInputTextSyle,
                        decoration: buildDarkInputDecoration(label: "Email"),
                      ),
                      const SizedBox(height: 16),
                      TextField(
                        obscureText: true,
                        controller: _passwordController,
                        style: defaultInputTextSyle,
                        decoration: buildDarkInputDecoration(label: "Senha"),
                      ),
                      const SizedBox(height: 20),
                      ElevatedButton(
                        onPressed: () {
                          // Agora não dará erro de null, pois os controllers existem
                          context.read<AuthViewModel>().login(
                                _emailController.text,
                                _passwordController.text,
                              );
                        },
                        style: ElevatedButton.styleFrom(
                          padding: const EdgeInsets.symmetric(
                              horizontal: 42, vertical: 12),
                        ),
                        child: const Text("Entrar"),
                      ),
                      const SizedBox(height: 16),
                      Center(
                        child: Row(
                          mainAxisAlignment: MainAxisAlignment.center,
                          children: [
                            _buildSocialIcon(context, 'assets/icons/facebook_icon.svg', 'Facebook'),
                            const SizedBox(width: 24),
                            _buildSocialIcon(context, 'assets/icons/gmail_icon.svg', 'Google'),
                            const SizedBox(width: 24),
                            _buildSocialIcon(context, 'assets/icons/x_icon.svg', 'X (Twitter)'),
                          ],
                        ),
                      ),
                      TextButton(
                        onPressed: () {},
                        child: const Text("Esqueceu a senha?"),
                      ),
                      TextButton(
                        onPressed: () {
                          Navigator.push(
                            context,
                            MaterialPageRoute(
                                builder: (context) => RegisterScreen()),
                          );
                        },
                        child: const Text("Primeiro acesso? Crie uma conta aqui"),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildSocialIcon(
      BuildContext context, String assetPath, String socialName) {
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
