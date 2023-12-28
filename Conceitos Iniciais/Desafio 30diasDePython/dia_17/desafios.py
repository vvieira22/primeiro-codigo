#1
#nao entendi direito o exercicio mas irei fazer da forma menos inteligente, utilizando enumerate.
nomes = ['Finlândia', 'Suécia', 'Noruega','Dinamarca','Islândia', 'Estônia','Rússia']
nordic_countries = []
ru = ""
es = ""

for index,nome in enumerate(nomes):
    if(index < 5):
        nordic_countries.append(nome)
    else:
        if(nome=="Rússia"):
            ru = nome
        else: #estonia
            es = nome
print(nordic_countries,es,ru)