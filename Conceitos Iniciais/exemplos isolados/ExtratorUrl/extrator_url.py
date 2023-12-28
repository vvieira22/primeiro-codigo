import re

class extratorUrl:
    def __init__(self = None, url = None, inicio_separador_param = None):
        
        if(inicio_separador_param == None):
            raise ValueError("Separador de inicio de parametro não definido")
        else:
            self._inicio_separador_param = inicio_separador_param

        self._url = self.tratar_url(url)
        self.validar_url(url)

    def validar_url(self, url):
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        resultado_match = padrao_url.match(url)

        if not resultado_match:
            raise ValueError("URL em formato incorreto")

    def tratar_url(self, url):
        if not url:
            raise ValueError("URL vazia")
        else:
            return url.strip()
    
    def get_url_parametros(self):
        _index_url_param = self._url.find(self._inicio_separador_param)
        _url_param = self._url[_index_url_param+1:]

        return _url_param

    def get_url_base(self):
        indice_separador_param = self._url.find(self._inicio_separador_param)
        _url_base = self._url[0:indice_separador_param]

        return _url_base

    def get_valor_parametro(self, parametro):
        indice_parametro = self.get_url_parametros().find(parametro)
        indice_valor = indice_parametro + len(parametro) + 1
        indice_separador_parametro = self.get_url_parametros().find('&', indice_valor)
        
        if indice_separador_parametro == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_separador_parametro]
        return valor

    def __len__(self):
        return len(self._url)

    # se eu dar um print no objeto ele vai vir pra ca
    def __str__(self):
        return "\nUrl: " + self._url + "\n" + "Parametros: " + self.get_url_parametros()
    
    # poder comparar objetos desse tipo
    def __eq__(self, other):
        return self._url == other._url


url = extratorUrl("bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real", "?")
url2 = extratorUrl("bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real", "?")

# is verifica se a identidade desse objeto é a mesma
# == compara valores iguais (não idênticos)
# print(url == url2)


DOLAR = 5.50
url = extratorUrl("bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real", "?")
moeda_origem = url.get_valor_parametro("moedaOrigem")
moeda_destino = url.get_valor_parametro("moedaDestino")
quantidade = int(url.get_valor_parametro("quantidade"))

if(moeda_origem == "real" and moeda_destino == "dolar"):
    print(f'{quantidade} reais = {quantidade/DOLAR:.3f} dolar')
elif(moeda_origem == "dolar" and moeda_destino == "real"):
   print(f'{quantidade} dolar = {quantidade * DOLAR:.3f} reais')
else:
    print(f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível.")