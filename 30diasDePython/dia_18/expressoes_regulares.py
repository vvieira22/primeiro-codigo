#Expressoes regular ou Regex é uma
#string de texto especial que ajuda a encontrar
#padroes nos dados.

#A regex pode ser utilizada para verificar algum tipo de padrao
#para usarmos em python devemos importar o modulo regex camado re.

import re

'''
re.match() : pesquisa apenas no início da primeira linha da string e retorna objetos correspondentes se encontrados, caso contrário retorna None.
re.search : Retorna um objeto de correspondência se houver um em qualquer lugar da string, incluindo strings multilinhas.
re.findall : Retorna uma lista contendo todas as correspondências
re.split : Pega uma string, divide-a nos pontos de partida, retorna uma lista
re.sub : Substitui uma ou mais correspondências dentro de uma string
'''

#Match
# re.match(substring,string,re.I)
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore
#  A função match retorna um objeto somente se o texto começar com o padrão.
txt = "eu adoro estudar python e programação em geral."

match = re.match("eu adoro",txt,re.I)
print(match)

#onde comeca a frase que deu match e onde tgermina
span = match.span()
start,end = span
print(start,end) # 0 - 8
substring = txt[start:end]
print(substring)


#Search
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match = re.search("most",txt,re.I)
print(match) #<re.Match object; span=(14, 18), match='most'>
print(match.span()) #14:18
#Search é melhor que o match pois retorna em qualquer posicao
#nao precisa iniciar a string, mas temos uma funcao ainda melhor.


#findall
#retorna todas as correspondências como uma lista
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']


#Por estarmos utilizando o re.I, letras maisculas e minusculas
#estão incluidas. Se nao tivermos usando o re.I, teriamos que escrever
#o nosso codigo de outra forma achar Python e python.
matches = re.findall('[Pp]ython', txt)
#ou
matches = re.findall('Python|python', txt)


#Substituindo uma substring.
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python','c#',txt,re.I)
print(match_replaced)

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt) #remove %
print(matches)


#Dividindo textos usando split Regex.

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
#retorna uma lista de cada elemento separado pelo \n achado na string.
print(re.split('\n', txt)) # splitting using \n - end of line symbol


#Padroes em regex.
#Usamos a declaracao r'string' para identificar regex.

regex_patter = r'apple'
txt = 'i love apple and banana.'
matches = re.findall(regex_patter,txt)
matches = re.findall(regex_patter,txt,re.I) # for Apple and apple
print(matches)

#Ou podemos utilizar regras para padrao
#usando r'[Aa]pple'
#Regras e caracteristicas regex pattern

'''

[]: Conjunto de caracteres
    [a-c] a,b ou c
    [a-z] qualquer letra entre a - z
    [A-Z] qualquer letra entre A - Z
    [0-3] 0 or 1 or 2 or 3
    [0-9] qualquer número entre 0 - 9
    [A-Za-z0-9] qualquer caractere único, de a-z, de A-Z ou de 0-9

\: usa para escapar de caracteres especiais
    \d significa: corresponde onde a string contém dígitos (números de 0 a 9)
    \D significa: corresponde onde a string não contém dígitos

. : qualquer caractere (exceto de nova linha \n)

^ : começa com
    r'^substring' por exemplo r'^love', uma frase que começa com a palavra amor
    r'[^abc] significa não a, não b, não c.

$ : termina com
    r'substring$" por exemplo r'love$' frase que termina com frase love.

* : zero ou mais vezes
    r'[a]* opcional ou pode ocorrer várias vezes.

+ : uma ou mais vezes
    r'[a]+' significa pelo menos uma vez (ou mais)

? : zero ou uma vez
    r'[a]?' significa zero ou uma vez

{3} :   Exatamentee 3 caracteres.
{3,} :  Pelo menos 3 caracteres.
{3,8} : 3 a 8 caracteres

| : Ou
    r'maça|banana' significa ter maça ou apple

() : Capturar e agrupar.

'''


#Colchetes
#Iremos utilizar colchetes para incluir letras maisculas e minusculas.
pattern = r'[Aa]pple|[Bb]anana'
txt = 'apple ou Apple and banana ou Banana are a fruits.'
matches = re.findall(pattern,txt)
# print(matches) #apple,Apple,banana,Banana


#Caractere de escape (\) em RegEx
regex_pattern = r'\d'  # a significa digitos no regex
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1']

#Uma ou mais vezes (+)
regex_pattern = r'\d+'  # d is a special character which means digits, + mean one or more times
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['6', '2019', '8', '2021'] - now, this is better!


#Período - Period (.)
#Regex abaixo diz, caracter que começa com a até repeticao de qualquer caractere até " "
txt = '''Apple and banana are fruits'''
regex_pattern = r'[a].+'  # . any character, + any character one or more times 
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['and banana are fruits']

#Zero ou mais vezes (*)
regex_pattern = r'[a].*'  # . any character, * any character zero or more times 
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
# print(matches)  # ['and banana are fruits']

#Zero ou uma vez(?)
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']


#Quantificador em regex.
#Podemos especificiar o comprimento da substring que procuramos.
#Utilizando chaves {}. Vamos supor que queremos uama substring com 4 caracteres:
#Mais precisamente achar todos anos na string.

#exatos 4digitos.
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

#achar de 1 a 4 digitos.
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1, 4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']


# ^ Começa com.
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']

#Negacao
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']