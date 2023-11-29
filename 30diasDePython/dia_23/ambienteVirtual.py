# Configurando Ambientes Virtuais
# Para começar o projeto, seria melhor ter um ambiente virtual. 
# O ambiente virtual pode nos ajudar a criar um ambiente isolado ou separado. 
# Isso nos ajudará a evitar conflitos nas dependências entre projetos.
# Se você escrever pip freeze em seu terminal, verá todos os pacotes instalados 
# em seu computador.
# Se usarmos virtualenv, acessaremos apenas pacotes específicos
# para aquele projeto. Abra seu terminal e instale o virtualenv


#Depois de instalar virtualenv
# Crie um ambiente virtual com o nome que você quiser

# python -m venv virtualenvTeste

# Ative o ambiente virtual
# virtualenvTeste\Scripts\activate.bat

#Agora o diretorio no seu terminal ira comecar com o nome do seu ambiente virtual

#Verificando pacotes instalados no ambiente virtual
# pip freeze

#Depois de instalar um pacote especifico no ambiente virtual
#Voce pode sair do ambiente virtual com o comando
# deactivate

#Para voltar pro ambiente ja criado voce pode utilizar o comando:
# virtualenvTeste\Scripts\activate.bat