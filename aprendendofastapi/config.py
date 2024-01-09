import databases
import sqlalchemy
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///db.sqlite")
#VARIAVEL DE AMBIENTE, A APP VAI PEGAR
TESTE_DATABASE = os.getenv('TESTE_DATABASE', 'false') in ('true', 'yes')  #testes automatizados

database = databases.Database(DATABASE_URL, force_rollback = TESTE_DATABASE)
metadata = sqlalchemy.MetaData()
#FORCE_ROLLBACK NAO VAI GRAVAR OS DADOS que estao sendo gravados pela api, nao vai ser gravado no arquivo de verdade
