#1
#Achei melhor fazer com dict, pra nao ter repeticao de chaves.
import re
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
lista = paragraph.replace(".","").split(" ")
dicionario = {letra : lista.count(letra) for letra in lista}
dicionario_ordenado = {k: v for k, v in sorted(dicionario.items(), key=lambda item: item[1],reverse=True)}
# print(dicionario_ordenado)


#2
text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."
pattern_numbers = r'-?[0-9]+'
match = re.findall(pattern_numbers,text)
pointers = [int(x) for x in match]
sorted_p = sorted(pointers)
resultado = (sorted_p[-1])-(sorted_p[0])
# print(resultado)


#Level 2
#1
def is_val_var(variable):
    return True if re.findall((r'^[a-zA-Z]+_?[a-zA-Z]+$'),variable) else False

print(is_val_var("calabreso_junior"))
print(is_val_var("calabreso-junior"))
print(is_val_var("1calabreso_junior"))
print(is_val_var("calabresoJunior"))


#Level 3
#1
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
palavras = re.sub((r'[$]|%|@|&|$|;|#|[.]|[!]|[?]|[,]|'),"",sentence).split()
contagem = [(x, palavras.count(x)) for x in set(palavras)]
print(sorted(contagem,reverse=True,key=lambda x: x[1])[0:3])
