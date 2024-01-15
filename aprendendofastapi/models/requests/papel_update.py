from typing import Optional,List
from pydantic import BaseModel

class PapelUpdate(BaseModel):
    nome :Optional[str] = None
    cnpj :Optional[str] = None