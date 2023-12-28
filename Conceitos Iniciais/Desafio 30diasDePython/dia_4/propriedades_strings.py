#Escape Sequences in Strings
#--------------------------------------------------------------------
"\n quebra de linha"
print("Quebra de \n linha")


'''\r quebra de linha
diferente do \n, alguns sistema só aceitam \r ou \n\r
para quebra linha
'''
print("Quebra de \n linha")


"\t, tabulação de 8 espaços"
print("Tabulação \tde 8 espaços")


"\\, colocar \ no texto"
print("Colocando \\ no texto!")


"\' ou \", colocar ' no texto"
print("\'usando aspas simples\'")
print("\"usando aspas duplas\"")
#--------------------------------------------------------------------


#String Formmating using .format
#--------------------------------------------------------------------
#":.2f" para limitar casas decimais do float format.

meu_nome = 'Maicon'
sobrenome = 'douglas'
idade = 28
altura = 1.789890

formated_string = "Eu sou {} {}\ntenho {} anos\ncom {:.2f} de altura".format(meu_nome,
sobrenome,idade,altura)

print(formated_string)
#--------------------------------------------------------------------

#String Interpolation / f-Strings (Python 3.6+)

print(f'Meu nome é {meu_nome} {sobrenome}\ntenho {idade} anos, e altura de {altura:.2f}')
#--------------------------------------------------------------------

#Acessando caracteres em strings por índice

#Começa pelo valor 0 da string.
#e inversamente com -1 até -n()
"""
'python'      'python' 
'012345'      -'654321'
"""

#exemplo, mostrar a letra 'p' da string python
nome_linguagem='python'
print(nome_linguagem[0])
print(nome_linguagem[-6])
#--------------------------------------------------------------------


#Slice Python Strings
'''
S[A:B]

>S- variável que referencia a String
>A- início do intervalo
>B- final do invertalo (excluindo o último caractere)

Omitindo o valor de A automaticamente é definido como 0 (inicio)
Omitindo B, vai até o final da string.
Omitindo ambos vai pegar tudo
'''

#mostrar últimas duas letras de uma string 
print(nome_linguagem[-2:])

'''
S[A:B:C]

>S- variável que referencia a String
>A- início do intervalo
>B- final do invertalo (excluindo o último caractere)
>C- Passo (quando pular) dentro do intervalo
'''
#mostrar letras pulando em 1 em 1
print(nome_linguagem[::2])

#inverter string modo 1
print(nome_linguagem[-1:0-(len(nome_linguagem)+1):-1])
#inverter string modo 2
print(nome_linguagem[::-1])
#--------------------------------------------------------------------

#String Methods

#capitalize(): Converts the first character of the string to capital letter

#count(): número de vezes que aparece uma substring count(substring,start,end)
nome_variavel = "maicon douglas"
print(f'numero de vezes que aparece a letra o:  {nome_variavel.count("o",0,len(nome_variavel)-1)}')

#endswith(): Checks if a string ends with a specified ending. return (true or false)

#expandtabs(): Replaces tab character (\t) with spaces, 
#default tab size is 8. It takes tab size argument
nome_variavel_extra ='thirty\tdays\tof\tpython' 
print(nome_variavel_extra.expandtabs(1))


# find(): Returns the index of the first occurrence of a substring, if not found returns -1
nome_variavel = "o rato roeu a roupa do rei de roma"
print(nome_variavel.find("r"))

# rfind(): Returns the index of the last occurrence of a substring, if not found returns -1

# format(): formats string into a nicer output 
nome = 'vitor'
idade = 21
formacao = 'desenvolvedor'

sentenca = 'Eu sou {} tenho {} anos e sou {}.'.format(nome,idade,formacao)
print(sentenca)

#index(): Returns the lowest index of a substring, additional arguments indicate starting and ending 
# index (default 0 and string length - 1) If the substring is not found it raises a valueError.

#rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending 
# index (default 0 and string length - 1)

#isalnum(): Checks alphanumeric character. return true or false
#um caractere que é uma letra ou um número.
print('vitor 22'.isalnum())

#isalpha() Checks if all string elements are alphabet characters (a-z and A-Z)

print("Vitor".isalpha())

#isdecimal(): Checks if all characters in a string are decimal (0-9)
challenge = '12 3'
print(challenge.isdecimal())  # False, space not allowed

#isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)

#isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), 
# just accepts more symbols, like ½)

#isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name

#islower(): Checks if all alphabet characters in the string are lowercase

#isupper(): Checks if all alphabet characters in the string are uppercase

#join(): Returns a concatenated string
linguagens = ['c','c++','java']
print(''.join(linguagens)) #onde ta '', se colocar algo, esse algo vai ficar na frente de cada elemento

print('|'.join(linguagens))

#strip(): Removes all given characters starting from the beginning and end of the string

challenge = 'testando o som'
print(challenge.strip('som')) # 'testando o'

#replace(): Replaces substring with a given string

challenge = 'Testando o jogo'
print(challenge.replace('jogo', 'som')) # 'Testando o som'

#split(): Splits the string, using given string or space as a separator
linguagens = "Java c c++ c#"
print(linguagens.split())

#title(): Returns a title cased string (deixar todas as palavras com a primeira letra maiuscula)
challenge = '30 dias de python'
print(challenge.title()) # Thirty Days Of Python

#swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

#startswith(): Checks if String Starts with the Specified String. return true or false
challenge = "vitor é um desenvolvedor"
print(challenge.startswith("vitor"))

#--------------------------------------------------------------------
