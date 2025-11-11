import 'package:flutter/material.dart';
import 'app_colors.dart'; // Certifique-se de ter suas cores aqui

// ------------------------------------------------------------------
// CORES E CONSTANTES DE ESTILO GLOBAIS
// ------------------------------------------------------------------

const Color _baseColor = Colors.white70;
// Usando sua AppColors.primaryColor para o destaque de foco
final Color _primaryFocusColor = Colors.transparent;
const Color _fillColor = Color(0xFF1E1E1E); // Fundo do TextField

// Estilo da Borda Padrão
const OutlineInputBorder _baseBorder = OutlineInputBorder(
  borderRadius: BorderRadius.all(Radius.circular(8)),
  borderSide: BorderSide(color: _baseColor, width: 1.0),
);

// Estilo da Borda Focada (Material 3)
final OutlineInputBorder _focusedBorder = OutlineInputBorder(
  borderRadius: const BorderRadius.all(Radius.circular(8)),
  borderSide: BorderSide(color: _primaryFocusColor, width: 2.0),
);


// ------------------------------------------------------------------
// EXPORTANDO O TEMA MODULAR (A Chave da Solução)
// ------------------------------------------------------------------

/// Retorna um [InputDecorationTheme] customizado para o Dark Mode.
/// Use com Theme.of(context).copyWith(inputDecorationTheme: darkTextFieldTheme);
InputDecorationTheme get darkTextFieldTheme {
  return InputDecorationTheme(
    // Cores e Preenchimento
    filled: true,
    fillColor: _fillColor,
    isDense: true,

    // Estilo do Label (Email/Senha)
    labelStyle: const TextStyle(color: Colors.red),

    // Estilo das Bordas
    border: _baseBorder,
    enabledBorder: _baseBorder,
    focusedBorder: _focusedBorder,
  );
}

// ------------------------------------------------------------------
// EXPORTANDO UM InputDecoration (Para uso direto e pontual)
// ------------------------------------------------------------------

/// Retorna um [InputDecoration] customizado para uso direto em um único TextField.
InputDecoration buildDarkInputDecoration({required String label}) {
  return InputDecoration(
    labelText: label,
    labelStyle: const TextStyle(color: Colors.blue),

    filled: true,
    fillColor: _fillColor,
    isDense: true,

    border: _baseBorder,
    enabledBorder: _baseBorder,
    focusedBorder: _focusedBorder,
  );
}