import 'package:flutter/material.dart';
import 'package:silk_deaths/enums/auth_status.dart';
import 'package:silk_deaths/screens/recover_password_screen.dart';
import '../l10n/app_localizations.dart';
import '../models/User.dart';
import '../services/auth/auth_local.dart';
import '../theme/app_colors.dart';
import '../theme/app_textfield_style.dart';

class RecoverPasswordScreen extends StatelessWidget {
  RecoverPasswordScreen({super.key});

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
                          'assets/icons/icon_launcher.png',
                          width: 340,
                          height: 150,
                        ),
                        const SizedBox(height: 16),

                        // 1. TextFormField (com validator)
                        TextFormField(
                          controller: _nomeControler,
                          style: defaultInputTextSyle,
                          decoration: buildDarkInputDecoration(
                            label: AppLocalizations.of(context)!.fullName,
                          ),
                          validator: (value) {
                            if (value == null || value.trim().isEmpty) {return AppLocalizations.of(context)!.typeFullName;}
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

                        TextFormField(
                          controller: _passwordControler,
                          obscureText: true,
                          style: defaultInputTextSyle,
                          decoration: buildDarkInputDecoration(
                            label: AppLocalizations.of(context)!.newPassword,
                          ),
                          validator: (value) {
                            if (value == null || value.isEmpty) {return AppLocalizations.of(context)!.typeAPassword;}
                            if (value.length < 6) {return AppLocalizations.of(context)!.minimumCaracters;}
                            return null;
                          },
                        ),
                        const SizedBox(height: 16),

                        TextFormField(
                          obscureText: true,
                          style: defaultInputTextSyle,
                          decoration: buildDarkInputDecoration(
                            label: AppLocalizations.of(context)!.adminPassword,
                          ),
                          validator: (value) {
                            if (value != "admin123") {return AppLocalizations.of(context)!.adminPasswordIncorrectly;}
                            return null;
                          },
                        ),
                        const SizedBox(height: 16),

                        Row(
                          mainAxisAlignment: MainAxisAlignment.spaceBetween,
                          children: [
                            ElevatedButton(
                              onPressed: () {
                                Navigator.pop(context);
                              },
                              style: ElevatedButton.styleFrom(
                                padding: const EdgeInsets.symmetric(
                                  horizontal: 42,
                                  vertical: 12,
                                ),
                              ),
                              child: Text(AppLocalizations.of(context)!.back),
                            ),
                            const SizedBox(width: 16),
                            ElevatedButton(
                              onPressed: () {
                                // 1. VALIDA TUDO COM O FORM
                                if (_formKey.currentState!.validate()) {
                                  // 2. SÓ ENTRA AQUI SE TUDO ESTIVER OK
                                  _authLocal
                                      .resetPassword(
                                      _emailControler.text.trim(),
                                      _passwordControler.text,
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
                                          title: Text(AppLocalizations.of(context)!.success),
                                          content: Text(AppLocalizations.of(context)!.madeALoginToContinue),
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
                                              child: Text(AppLocalizations.of(context)!.ok),
                                            ),
                                          ],
                                        ),
                                      );
                                    }
                                  });
                                }
                              },
                              style: ElevatedButton.styleFrom(
                                padding: const EdgeInsets.symmetric(
                                  horizontal: 42,
                                  vertical: 12,
                                ),
                              ),
                              child: Text(AppLocalizations.of(context)!.confirm),
                            ),
                          ],
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