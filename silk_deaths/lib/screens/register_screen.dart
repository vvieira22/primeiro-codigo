import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../services/auth/auth_firebase.dart';

class RegisterScreen extends StatelessWidget {
  RegisterScreen({super.key});

  final TextEditingController? _emailControler = TextEditingController();
  final TextEditingController?  _nomeControler = TextEditingController();
  final TextEditingController? _passwordControler = TextEditingController();
  final TextEditingController?  _confirmpasswordControler = TextEditingController();

  AuthFirebase _authFirebase = AuthFirebase();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        padding: EdgeInsets.all(16),
        color: Colors.blue, // Cor de fundo da tela
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(
                padding: EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(16),
                ),
                child: Column(
                  children: [
                    FlutterLogo(size: 64),
                    SizedBox(height: 16),
                    TextField(
                      controller: _nomeControler,
                      decoration: InputDecoration(
                        labelText: "Nome Completo",
                        border: OutlineInputBorder(),
                      ),
                    ),
                    SizedBox(height: 16),
                    TextField(
                      controller: _emailControler,
                      decoration: InputDecoration(
                        labelText: "Email",
                        border: OutlineInputBorder(),
                      ),
                    ),
                    SizedBox(height: 16),
                    TextField(
                      obscureText: true,
                      controller: _passwordControler,
                      decoration: InputDecoration(
                        labelText: "Senha",
                        border: OutlineInputBorder(),
                      ),
                    ),
                    SizedBox(height: 16),
                    TextField(
                      obscureText: true,
                      controller: _confirmpasswordControler,
                      decoration: InputDecoration(
                        labelText: "Confirme sua senha.",
                        border: OutlineInputBorder(),
                      ),
                    ),
                    SizedBox(height: 16),
                    ElevatedButton(
                      onPressed: () {
                        if (_passwordControler!.text ==
                            _confirmpasswordControler!.text) {
                          _authFirebase
                              .cadastrarUsuario(
                                nome: _nomeControler!.text,
                                email: _emailControler!.text,
                                senha: _passwordControler!.text,
                              )
                              .then((String? error) {
                                if (error != null) {
                                  ScaffoldMessenger.of(context).showSnackBar(
                                    SnackBar(
                                        content:
                                        Text(error),
                                        backgroundColor: Colors.red
                                    ),
                                  );
                                } else {
                                  showDialog(
                                    context: context,
                                    builder: (context) => AlertDialog(
                                      title: Text(
                                        "Cadastro realizado com sucesso",
                                      ),
                                      content: Text(
                                        "Faça login para continuar",
                                      ),
                                      actions: [
                                        TextButton(
                                          onPressed: () =>
                                              Navigator.of(context).pop(),
                                          child: Text("OK"),
                                        ),
                                      ],
                                    ),
                                  );
                                }
                              });
                        }
                        else{
                          ScaffoldMessenger.of(context).showSnackBar(
                            SnackBar(
                                content:
                                Text("As senhas não coincidem"),
                                backgroundColor: Colors.red
                            ),
                          );
                        }
                      },
                      style: ElevatedButton.styleFrom(
                        padding: EdgeInsets.symmetric(
                          horizontal: 42,
                          vertical: 12,
                        ),
                      ),
                      child: Text("Cadastrar"),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
