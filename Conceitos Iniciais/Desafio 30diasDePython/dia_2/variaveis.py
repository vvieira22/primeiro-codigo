#'Dia 2: 30 dias de programação python'


#level 1
#--------------------------------------------------------------------
nome = "Maicon"
sobre_nome = "Silva"
nome_completo = "Maicon Silva"
pais = "Brasil"
cidade = "São Paulo"
idade = 70
ano = 2021
is_married = False
is_true = True
is_ligth_on = False
variavel1,variavel2,variavel3 = 10,"oi",10.222
#--------------------------------------------------------------------

#--------------------------------------------------------------------
#level 2
print(type(nome))
print(type(sobre_nome))
print(type(nome_completo))
print(type(pais))
print(type(cidade))
print(type(idade))
print(type(ano))
print(type(is_married))
print(type(is_true))
print(type(is_ligth_on))
print(type(variavel1),type(variavel2),type(variavel3))

print("Tamanho nome:",len(nome))
print("Tamanho Sobre Nome",len(sobre_nome))
#--------------------------------------------------------------------

#--------------------------------------------------------------------
primeiro_numero = 5
segundo_numero = 4

soma = primeiro_numero-segundo_numero
subtracao = primeiro_numero-segundo_numero
multipliacao = primeiro_numero*segundo_numero
divisao = primeiro_numero/segundo_numero
divisao_modulo = primeiro_numero%segundo_numero
potencia = primeiro_numero**segundo_numero
divisao_floor = primeiro_numero//segundo_numero
#--------------------------------------------------------------------

#--------------------------------------------------------------------
raio_circulo = 30
area_circulo = 3.14*raio_circulo**2
circuferencia_circulo = 2*3.14*raio_circulo

raio_circulo_digitada = int(input("Qual área do circulo?"))
print("A área do circulo para o raio digitado é:",3.14*raio_circulo_digitada**2)
#--------------------------------------------------------------------

#--------------------------------------------------------------------
nome_digitado = input("Qual o seu nome ?")
sobrenome_digitado = input("Qual o seu sobrenome?")
pais_digitado = input("Qual o seu país?")
cidade_digitado = input("Qual a sua cidade?")
idade_digitada = int(input("Qual a sua idade?"))
#--------------------------------------------------------------------

help('keywords')