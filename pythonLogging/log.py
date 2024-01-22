import functools
import logging

def log(log_type):
    logging.basicConfig(level=log_type,filename="log.txt",format="%(levelname)s:%(message)s")
    #posso passar file name direto no basicConfig
    logger = logging.getLogger()
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)
            logger.log(log_type, f"function {func.__name__} args: ({signature})")
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                logger.exception(f"Ocorreu um erro na função: {func.__name__}. ({str(e)})")
                raise e
        return wrapper
    return decorator

@log(logging.WARNING)
def funcaoSoma(n1,n2):
    raise(Exception("Erro na função"))

funcaoSoma(1,2)