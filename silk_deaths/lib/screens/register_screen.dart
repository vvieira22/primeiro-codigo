import 'package:flutter/material.dart';
import 'package:silk_deaths/enums/auth_status.dart';
import '../models/User.dart';
import '../services/auth/auth_local.dart';
import '../theme/app_colors.dart';
import '../theme/app_textfield_style.dart';

class RegisterScreen extends StatelessWidget {
  RegisterScreen({super.key});

  final TextEditingController _emailControler = TextEditingController();
  final TextEditingController _nomeControler = TextEditingController();
  final TextEditingController _passwordControler = TextEditingController();
  final TextEditingController _confirmpasswordControler = TextEditingController();

  final AuthLocal _authLocal = AuthLocal();

  // A KEY MÁGICA
  final _formKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomInset: true,
      body: Container(
        padding: const EdgeInsets.all(16),
        color: Colors.black,
        child: Center(
          child: SingleChildScrollView(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Form(
                  key: _formKey,
                  child: Container(
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(
                      color: AppColors.backgroundElementsColor,
                      borderRadius: BorderRadius.circular(16),
                    ),
                    child: Column(
                      children: [
                      Image.asset(
                      'assets/icons/icon_launcher.png', // Caminho para a sua imagem
                      width: 340,
                      height: 150,
                    ),
                        const SizedBox(height: 16),

                        // 1. TextFormField (com validator)
                        TextFormField(
                          controller: _nomeControler,
                          style: defaultInputTextSyle,
                          decoration: buildDarkInputDecoration(
                            label: "Nome Completo",
                          ),
                          validator: (value) {
                            if (value == null || value.trim().isEmpty) {return 'Digite seu nome completo';}
                            return null;
                          },
                        ),
                        const SizedBox(height: 16),

                        // 2. Email com validação
                        TextFormField(
                          controller: _emailControler,
                          keyboardType: TextInputType.emailAddress,
                          style: defaultInputTextSyle,
                          decoration: buildDarkInputDecoration(
                            label: "Email",
                          ),
                          validator: (value) {
                            if (value == null || value.isEmpty) {return 'Digite seu email';}
                            if (!value.contains('@') || !value.contains('.')) {return 'Email inválido';}
                            return null;
                          },
                        ),
                        const SizedBox(height: 16),

                        // 3. Senha
                        TextFormField(
                          controller: _passwordControler,
                          obscureText: true,
                          style: defaultInputTextSyle,
                          decoration: buildDarkInputDecoration(
                            label: "Senha",
                          ),
                          validator: (value) {
                            if (value == null || value.isEmpty) {return 'Digite uma senha';}
                            if (value.length < 6) {return 'Mínimo 6 caracteres';}
                            return null;
                          },
                        ),
                        const SizedBox(height: 16),

                        // 4. Confirmar senha
                        TextFormField(
                          controller: _confirmpasswordControler,
                          obscureText: true,
                          style: defaultInputTextSyle,
                          decoration: buildDarkInputDecoration(
                            label: "Confirme sua senha",
                          ),
                          validator: (value) {
                            if (value != _passwordControler.text) {return 'Senhas não coincidem';}
                            return null;
                          },
                        ),
                        const SizedBox(height: 16),

                        // BOTÃO COM VALIDAÇÃO AUTOMÁTICA
                        ElevatedButton(
                          onPressed: () {
                            // 1. VALIDA TUDO COM O FORM
                            if (_formKey.currentState!.validate()) {
                              // 2. SÓ ENTRA AQUI SE TUDO ESTIVER OK
                              _authLocal
                                  .registerUser(
                                User(
                                  name: _nomeControler.text.trim(),
                                  email: _emailControler.text.trim(),
                                  password: _passwordControler.text,
                                ),
                              )
                                  .then((AuthStatus response) {
                                if (!response.isSuccess) {
                                  ScaffoldMessenger.of(context).showSnackBar(
                                    SnackBar(
                                      content: Text(response.message),
                                      backgroundColor: Colors.red,
                                    ),
                                  );
                                } else {
                                  showDialog(
                                    context: context,
                                    builder: (context) => AlertDialog(
                                      title: const Text("Sucesso!"),
                                      content: const Text("Faça login para continuar"),
                                      actions: [
                                        TextButton(
                                          onPressed: () {
                                            _formKey.currentState?.reset();
                                            _nomeControler.clear();
                                            _emailControler.clear();
                                            _passwordControler.clear();
                                            _confirmpasswordControler.clear();
                                            // Remove o foco de qualquer campo de texto
                                            FocusScope.of(context).unfocus();
                                            Navigator.pop(context);
                                          },
                                          child: const Text("OK"),
                                        ),
                                      ],
                                    ),
                                  );
                                }
                              });
                            }
                            // Se não validar → mostra erros automaticamente
                          },
                          style: ElevatedButton.styleFrom(
                            padding: const EdgeInsets.symmetric(
                              horizontal: 42,
                              vertical: 12,
                            ),
                          ),
                          child: const Text("Cadastrar"),
                        ),
                      ],
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}