enum StatusPagamento { PENDENTE, APROVADO, REJEITADO }

void main() {
  StatusPagamento status = StatusPagamento.APROVADO;
  print('O status do pagamento é: $status');
  switch (status) {
    case StatusPagamento.PENDENTE:
      print('O pagamento está pendente.');
      break;
    case StatusPagamento.APROVADO:
      print('O pagamento foi aprovado.');
      break;
    case StatusPagamento.REJEITADO:
      print('O pagamento foi rejeitado.');
      break;
  }
  ;
  //Importante para salvar em um banco de dados
  print(status.index); // Exibe o índice do status
  print(StatusPagamento.values[1]); // Exibe o status correspondente ao índice 1
}
