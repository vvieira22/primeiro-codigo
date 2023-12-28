#like a c
lista_de_numeros = [19,99,232,22,3,55676,1221,5511,212121,991221]
maior = lista_de_numeros[0]

for i in range(0,len(lista_de_numeros)):
    if(lista_de_numeros[i]>maior):
        maior=lista_de_numeros[i]
print(maior)

#like a python
print(max(lista_de_numeros))