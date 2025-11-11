class User {
  int? id;
  String name;
  String email;
  String password;

  User({
    this.id,
    required this.name,
    required this.email,
    required this.password
  });

  // 1. Converte o objeto Dart (Usuario) em um Map (necessário para INSERIR no DB).
  Map<String, dynamic> toMap() {
    return {
      // 'id' não é incluído aqui se o objeto for novo, pois o DB gera ele.
      'id': id,
      'name': name,
      'email': email,
      'password': password,
    };
  }

  // 2. Converte o Map (retornado pelo DB) em um objeto Dart (Usuario).
  // Um construtor 'factory' é um tipo especial de construtor em Dart.
  // Diferente de um construtor normal (como o 'User({...})' lá de cima), um
  // construtor 'factory' não precisa criar uma nova instância da classe *sempre*.
  // Ele pode, por exemplo, retornar uma instância já existente ou, como neste caso,
  // delegar a criação para outro construtor.
  // Aqui, usamos 'factory' para criar um objeto 'User' a partir de um 'Map'. É uma convenção comum para deserialização de dados (ex: de JSON ou banco de dados).
  factory User.fromMap(Map<String, dynamic> map) {
    return User(
      id: map['id'] as int?,
      name: map['name'] as String,
      email: map['email'] as String,
      password: map['password'] as String,
    );
  }
}