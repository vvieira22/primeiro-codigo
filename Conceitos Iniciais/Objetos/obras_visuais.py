class ProducaoAudioVisual:
    def __init__(self, nome, ano_lancamento, classificacao):
        self._nome = nome.title()
        self._ano_lancamento = ano_lancamento
        self._classificacao = classificacao
        self._likes = 0

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome_filme(self, nome):
        self._nome = nome

    @property
    def ano_lancamento(self):
        return self._ano_lancamento
    @ano_lancamento.setter
    def ano_lancamento(self, ano_lancamento):
        self._ano_lancamento = ano_lancamento 

    @property
    def likes(self):
        return self._likes
    
    def dar_like(self):
        self._likes += 1   

class Filme(ProducaoAudioVisual):
    def __init__(self, nome = None, ano_lancamento = None, classificacao = None, duracao = None):
        #chamando construtor da classe "mãe" 
        super().__init__(nome, ano_lancamento, classificacao)
        self.duracao = duracao

    #sempre colocar essa nomeclatura para metodos exclusivos da classe "filha"
    @classmethod
    def metodo_expecifico_para_class(cls):
        pass
    
    #O método estático é acessível a partir da classe e também da instância.
    @staticmethod
    def log():
        pass

    #The __str__ é  uma representação de string de um objeto
    #Podemos ter o __repr__, que é usado para mostrar uma representação que ajude no debug ou log de um código.
    #Esse último vai printar literalmente o que foi definido. (geralmente usado para debugar e gerar log)
    def __str__(self):
        return f'\nNOME: {self._nome}\nANO: {self._ano_lancamento}\nClassificação: {self._classificacao}\nDuração: {self.duracao}m'

class Serie(ProducaoAudioVisual):
    def __init__(self, nome = None, ano_lancamento = None, classificacao = None, temporadas = None):
        super().__init__(nome, ano_lancamento, classificacao)
        self.__temporadas = temporadas

    @property
    def temporadas(self):
        return self.__temporadas
    @temporadas.setter
    def temporadas(self, temporadas):
        self.__temporadas = temporadas 

    def __str__(self):
        return f'\nNOME: {self._nome}\nANO: {self._ano_lancamento}\nClassificação: {self._classificacao}\nTemporadas: {self.temporadas}'

class Playlist():
    def __init__(self, nome, lista_producao_audio_visual = None):
        self._lista_producao_audio_visual = lista_producao_audio_visual
        self.nome = nome
    
    #metodo que define que é um iterável
    def __getitem__(self, item):
        return self._lista_producao_audio_visual[item]
    
    def __len__(self):
        return len(self._lista_producao_audio_visual)

    @property
    def listagem(self):
        return self._lista_producao_audio_visual

    @property
    def tamanho_lista(self):
        return len(self._lista_producao_audio_visual)


#Duck Typing refere-se ao princípio de não restringir ou vincular o código a tipos de dados específicos .
#fazer nosso objeto passar a ser um tipo expecifico , não quero ser daquele tipo, mas sim desejo me comportar como aquele tipo
#existem alguns mais famosos, segue imagem "data_model.png" no documento.
#No Python, não é preciso herdar de uma classe específica pra ter polimorfismo. 
# O que é importante no Python é: se você quer um iterável, devo se preocupar com o que um iterável deve fazer.
#O nome dessa característica é duck typing.


vingadores = Filme("vingadores guerra de ultron", "2017", "14", "160")
vingadores.dar_like()

homem_aranha = Filme("homem aranha 1", "2002", "livre", "176")
homem_aranha.dar_like()
homem_aranha.dar_like()

homem_aranha2 = Filme("homem aranha 2", "2005", "livre", "156")
the_walking_dead = Serie("the walking dead", "2014", "18", "9")
breaking_bad = Serie("breaking bad", "2013", "16", "7")
stranger_things = Serie("stranger things", "2016", "12", "4")

lista_filmes_e_series = [vingadores, homem_aranha, homem_aranha2, the_walking_dead, breaking_bad, stranger_things]
playlist_vitor = Playlist("filmes e series geek", lista_filmes_e_series)
print(len(playlist_vitor))
# for programas_audio_visuais in playlist_vitor:
#     print(programas_audio_visuais)