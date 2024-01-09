Vamos utilizar o ambiente chamado aprendendofastapi

    python -m venv aprendendofastapi   -criar
    aprendendofastapi\Scripts\activate  =ativar e entrar ambiente
    deactivate - sair para ambiente padrao.

uvicorn main:app --reload
* o --reload serve para qualquer alteracao no main.py aplicar automaticamente.
* interessante apenas em ambiente de desenvolvimento.

#main app tem exemplos iniciais de uma api, com explicacoes etc..

#main2 api simples feita para utilizar.

Uma forma interessante de manegar ambientes virtuais e saber quais versoes corretas
é exportando um txt com todos as dependencias listadas.

. pip3 freeze -> requerimentos.txt   (vai salvar em um .txt)

Voce pode mover esse txt para outro computador e digitar o seguinte para instalar todos

. pip3 install -r requerimentos.txt