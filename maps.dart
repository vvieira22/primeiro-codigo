 void main(){
  // Declarando um Map (Chave/Valor)
  Map<String, double> salarios = {
    'gerente': 19345.78,
    'estagiario': 600.00,
    'pleno': 10000.00,
  };
  salarios.remove('pleno');
  print(salarios);
  print(salarios.length);
  print(salarios['gerente']);
  print(salarios.keys);
  print(salarios.values);
  print(salarios.entries);
  print(salarios.containsKey("gerente"));
  print(salarios.containsValue(10));
  print(salarios.isEmpty);

  //Aumento de 10% para todo mapa
  salarios.forEach((chave,valor) => salarios[chave] = valor * 1.1);
  print(salarios);

  // BOTA O ! no final quando vc tem certeza que tem o valor certo, e nao nulo !!!!!
  double valorCertezaqueNaoEnULO = salarios["gerente"]!;
  print(valorCertezaqueNaoEnULO);

  //Caso nao saiba ou tenha duvida, bote valor padrao caso n ache
  double valorXSeNaoTiverY = salarios["junior"] ?? 0.0;
  print(valorXSeNaoTiverY);
}