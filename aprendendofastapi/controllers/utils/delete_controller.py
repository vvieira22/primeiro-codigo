import ormar
from controllers.utils.entidade_nao_encontrada import entidade_nao_encontrada
from functools import wraps
#Generalizar o delete controller para qualquer modelo
#Só irei fazer do delete a titulo de curiosidade, de como generalizar
def delete_controller(modelo: ormar.Model):
    def inner(func):
        @entidade_nao_encontrada
        @wraps(func)
        async def wrapper(id: int):
            entidade = await modelo.objects.get(id=id)
            return await entidade.delete()
        return wrapper
    return inner