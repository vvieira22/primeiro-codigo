ages = [19, 22, 19, 24, 20, 25, 26, 21, 25, 24,29,22]
ages_ordenado  = sorted(ages)

#minima
minimo = min(ages_ordenado)
print(minimo)

#maximo
maximo = max(ages_ordenado)
print(maximo)

ages_ordenado.append(minimo)
ages_ordenado.append(maximo)

#mediana das idades
ages_ordenado = sorted(ages_ordenado)

print(ages_ordenado)

index_meio = len(ages_ordenado)//2

if(len(ages_ordenado) % 2):
    print(ages_ordenado[index_meio])
else:
    print( (ages_ordenado[index_meio] + ages_ordenado[index_meio -1]) / 2.0)

#media
media = 0
for numeros in ages_ordenado:
    media += numeros
print(media)

#maximo menos minimo
maximo = max(ages_ordenado)
minimo = min(ages_ordenado)
print(maximo - minimo)

#minimo - media e maximo - media
print(abs(minimo - media))
print(abs(maximo - media))
