#1
dog = {}

#2
dog = {'viralata':["caramelo","15","4"],"rottweiler":["misto","19","4"]}

#3
aluno = {"nome":"vitor","idade":"19","sexo":"masculino","habilidades":["t.i","progracao"]}

#4
len(aluno)

#5
print(aluno["habilidades"])

#6
aluno["habilidades"].append("futebol")
print(aluno)

#7
print(aluno.keys)

#8
print(aluno.values())

#9
lista_tupla = aluno.items()

#10
aluno.pop("nome")

#11
del aluno