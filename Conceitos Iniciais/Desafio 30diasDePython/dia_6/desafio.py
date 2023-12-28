#1
tpl = tuple()

#2
irmaos_imaginarios = ('joao','jose','thiago')
irmas_imaginarias = ('joaquina','bia')

#3
irmaos = irmaos_imaginarios + irmas_imaginarias

#4
print(len(irmaos))

#5
pais = ('pai','mae')
familia = irmaos + pais

#Nível 2

#1
irmaos_descompactados = familia[0:len(irmaos)]
pais_descompactados = familia[len(irmaos):]
#segunda forma
pais_descompactados2 = familia[-len(pais):]

#2 
frutas = ('pera','maça','uva')
vegetais = ('cenoura','alface','pimentao')
animal = ('ovo','leite','carne')
food_stuff_tp = frutas + vegetais + animal

#3
food_stuff_tp = list(food_stuff_tp)

#4
item_do_meio =  food_stuff_tp[(int(len(food_stuff_tp)/2))]

#5
tres_primeiros = food_stuff_tp[:3]
tres_ultimos = food_stuff_tp[-3:]

#6
del food_stuff_tp

#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
