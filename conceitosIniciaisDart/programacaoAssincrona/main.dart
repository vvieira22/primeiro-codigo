//Exemplo de callbacs
void main2() {
  print('Início do programa');

  reqUsuario().then((encontrouUsuario) {
    print('Usuário encontrado: $encontrouUsuario');
    print(autenticarUsuario);
  });

  print('Fim do programa');
}

void main() async {
  print("inicio");
  bool sucesso =
      await auxiliar(); //podemos fazer dessa forma para travar o codigo ate finalizar,
  //ou entao usando .then para callbacks
  print("fim $sucesso");
}

//Precisa ter retorno Future pq é uma funcao assincrona
Future<bool> auxiliar() async {
  String usuario = await reqUsuario(); //esperar
  try {
    bool sucesso = await autenticarUsuario(usuario);
    return sucesso;
  } catch (e) {
    print(e);
    return false;
  }
}

Future<String> reqUsuario() async {
  print('Requisitando dados do usuário...');
  await Future.delayed(Duration(seconds: 2));
  return "vitor";
}

Future<bool> autenticarUsuario(String usuario) async {
  if (usuario != "vitor") {
    throw Exception("Usuario inválido");
  }
  return true;
}
