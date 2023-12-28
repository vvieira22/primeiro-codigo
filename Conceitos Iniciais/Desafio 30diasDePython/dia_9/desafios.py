#1
input = int(input())
print("Você é maior de idade") if (input >=18) else print("aguarde mais um pouco")

# #2
my_age = 30
if(my_age >input):
    print("vc é mais velho")
elif(my_age == input):
    print("mesma idade")
else:
    print("eu sou mais velho")

#3
input_2 = int(input())
input_3 = int(input())

if(input_2 > input_3):
    print("a maior que b")
elif(input_3 > input_2):
    print("b maior que a")
else:
    print("igual")


#LEVEL 2
# 1
nota = int(input())
if(nota <=49):
    print("F")
elif(nota >=50 and nota <=59):
    print("D")
elif(nota >=60 and nota <=69):
    print("C")
elif(nota >=70 and nota <=89):
    print("B")
else:
    print("A")

#2
lista_outono = ["setembro","outubro","novembro"]
lista_inverno = ["dezembro","janeiro","fevereiro"]
lista_primavera = ["março","abril","maio"]
lista_verao = ["junho","julho","agosto"]

mes = input().lower()
if(mes in lista_outono):
    print("outono")
elif(mes in lista_inverno):
    print("inverno")
if(mes in lista_primavera):
    print("primavera")
else:
    print("verao")

#3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruta = input().lower()

print("fruta ja adicionada") if (fruta in fruits) else fruits.append(fruta) ; print(fruits)


#LEVEL 3
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'gen' : "W",
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
#1
print("tem key skills") if "skills" in person.keys() else print("nao tem")

#2
if "skills" in person.keys():
    print("tem") if "Python" in person["skills"] else print("nao tem")

#3
if "Javascript" and "React" in person["skills"]:
    print('He is a front end developer')
elif "Node" and "Python" and "MongoDB" in person["skills"]:
    print('He is a backend developer')
elif "React" and "Node " and "MongoDB" in person["skills"]:
    print('He is a fullstack developer')
else:
    print('unknown title')
    
if (person["is_marred"] and person["country"] == "Finland"):
    print(
        f'{person["first_name"]} {person["last_name"]} lives in {person["country"]} '
        f'{"He" if person["gen"] == "M" else "She"} is married.'
        )