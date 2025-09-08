void main() {
  // RepositorioPessoasRemote repositorio = RepositorioPessoasRemote();
}

//Tenho 2 tipos de acesso ao repositorio, remoto e local, se eu quiser trocar, eu tenho
//que garantir que os nomes sejam os mesmos do método se nao tem que mudar tudo, isso pode causar
//muito problema e retrabalho, entao vamos fazer um contrato, uma interface.
// class RepositorioPessoasRemote {
//   String ler(int i) {
//     return "Vitor";
//   }

//   void adicionar(String nome) {}

//   void apagar(int i) {}  
// }

// class RepositorioPessoaslocal {
  
//   String ler(int i) {
//     return "Vitor";
//   }

//   void adicionar(String nome) {}

//   void apagar(int i) {}  
// }

//Assim que faz, abstract e sem implementar os metodos so declarando.
abstract class RepositoPessoas {
  String ler(int i);
  void adicionar(String nome);
  void apagar(int i);
}
//Agora com o contrato feito, interface, vamos chamar em cada 1 tipo.

class RepositorioPessoasRemote implements RepositoPessoas {
  @override
  String ler(int i) {
    return "lendo da forma Remota";
  }
  @override
  void adicionar(String nome) {}
  
  @override
  void apagar(int i) {}  
}

class RepositorioPessoaslocal implements RepositoPessoas {
  
  @override
  String ler(int i) {
    return "lendo da forma local";
  }

  @override
  void adicionar(String nome) {}

  @override
  void apagar(int i) {}  
}

//Apartir daqui eu consigo sobreescrever e fazer da forma que eu quiser pq garante que o nome é o mesmo
//mas pode ter formas diferentes de implementar dentro de cada método que implementou a interface.