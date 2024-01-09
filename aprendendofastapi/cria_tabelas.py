import sqlalchemy
from config import DATABASE_URL, metadata
from models.papel import Papel  #importe para o ormar reconhecer o modelo

def configurar_banco(database_url = DATABASE_URL):
    print(database_url)
    engine = sqlalchemy.create_engine(database_url)
    metadata.drop_all(engine)
    metadata.create_all(engine)
    
if __name__ == "__main__":
    configurar_banco()