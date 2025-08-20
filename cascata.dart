void main() {
  //Metodos como esse aqui por exemplo geralmente retornam void impedindo de colocar
  //outros metodos na sequencia

  List<String> nomes = ['Ana', 'Bia', 'Gui', 'Lia', 'Rafa'];
  print(nomes);
  // nomes.add('Rebeca').remove('Ana'); // >>> nome.add retorna void, logo n da

  //MASSSS, temos uma safadeza que permite fazer isso retornando objeto original
  //usar ..
  List<String> stringAtualizada = nomes
    ..add('Rebeca')
    ..remove('Ana'); // aqui retornamos o objeto original
  print(nomes);
}
