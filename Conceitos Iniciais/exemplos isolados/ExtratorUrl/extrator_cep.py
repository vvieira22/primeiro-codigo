endereco = 'Rua otavio pinheiro 188, Magé, Rio de Janeiro, Bairro comendador reis, 25900189'

#como iriamos pegar o cep se o mesmo pode estar no final, ou em qualquer lugar do endereco fornecido?

import re #Regular Expression -- RegEx

#5 digitos + hífen(opcional)
#3 digitos finais
#? é opcional
padrao_cep = re.compile("[\d]{5}[-]?[\d]{3}")
busca = padrao_cep.search(endereco)  #retorna Match ou None

if(busca):
    print(busca.group())