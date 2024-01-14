from pydantic import BaseModel
import ormar
from config import database, metadata
from pydantic import validator
import re

class Papel(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "papeis"
        
    id: int = ormar.Integer(primary_key=True)
    nome: str = ormar.String(max_length=100)
    sigla: str = ormar.String(max_length=10)
    cnpj: str = ormar.String(max_length=20)
    
    @validator('sigla')
    def valida_formatacao_sigla(cls, v):
        pattern = r'^[a-zA-Z]{4}\d{1,2}$'
        if not re.compile(pattern).match(v):
            raise ValueError('A sigla deve ter até 4 letras e 2 números no final')
        return v
        