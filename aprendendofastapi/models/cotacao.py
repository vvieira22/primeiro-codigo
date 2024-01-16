import ormar
from config import database, metadata
import datetime
from models.papel import Papel
from typing import Optional

class cotacao(ormar.Model):
    class Meta:
        metadata=metadata
        database=database
        tablename="cotacoes"
        
    id: int = ormar.Integer(primary_key=True)
    valor: float = ormar.Float(minimum=0)
    horario: datetime = ormar.DateTime(timezone=False)
    papel : Optional[Papel] = ormar.ForeignKey(
        Papel,
        skip_reverse=True
    )
    
#ABDIQUEI DE USAR COTACAO POIS MEU CONHECIMENTO NESSE MOMEMENTO NAO ERA GRANDE
#ESTAVA COPIANDO E COLANDO O CÓDIGO SEM ENTENDER NADA DESSE RELACIONAMENTO COTACAO X PAPEIS.