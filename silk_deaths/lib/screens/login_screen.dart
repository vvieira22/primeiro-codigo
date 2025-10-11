import 'package:flutter/material.dart';
import 'package:flutter/services.dart';


class LoginScreen extends StatelessWidget {
  const LoginScreen({super.key});

  TextEditingController? get _emailControler => null;
  TextEditingController? get _passwordControler => null;

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
                    FlutterLogo(
                      size: 64,
                    ),
                    SizedBox(
                      height: 16,
                    ),
                    TextField(
                      controller: _emailControler,
                      decoration: InputDecoration(
                        labelText: "Email",
                        border: OutlineInputBorder(),
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
                      height: 16,
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
                      onPressed: () {},
                      child: Text("Primeiro acesso? Crie uma conta aqui"),
                    ),
                  ],
                )
              ),
            ],
          ),
        ),
      ),
    );
  }
}

