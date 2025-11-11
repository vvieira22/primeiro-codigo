enum AuthStatus {
  success,
  emailAlreadyExists,
  invalidCredentials,
  passwordMismatch,
  unknownError,
}

/// Extensão para facilitar mensagens de erro amigáveis
extension AuthStatusX on AuthStatus {
  String get message {
    switch (this) {
      case AuthStatus.success:
        return 'Operação realizada com sucesso!';
      case AuthStatus.emailAlreadyExists:
        return 'Este e-mail já está cadastrado.';
      case AuthStatus.invalidCredentials:
        return 'E-mail ou senha incorretos.';
      case AuthStatus.passwordMismatch:
        return 'As senhas não coincidem.';
      case AuthStatus.unknownError:
        return 'Ocorreu um erro inesperado. Tente novamente.';
    }
  }

  bool get isSuccess => this == AuthStatus.success;
  bool get isError => this != AuthStatus.success;
}