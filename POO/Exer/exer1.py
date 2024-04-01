## Avaliação e Média da Nota de Filmes

# Desenvolva novas funcionalidades para complementar o nosso gerenciamento da classe Filmes. Segue o escopo das funcionalidades:

# 1. Uma das funcionalidades requeridas é que o usuário possa realizar a avaliação de um filme 
# passando uma nota com parâmetro e que essa nota seja salva no atributo específico da classe.
# 2. Assim que uma avaliação for realizada, deve ser incrementado o total de avaliadores daquele filme. 
# Obs: Considere criar um atributo específico para esse fim.
# 3. Para cada filme ter uma nota de avaliação média que consiste na divisão do total de avaliação pelo total de avaliadores.

class Movie:
    def __init__(self, name, yearLaunch, includedPlan, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.avaliacaoTo = 0
        self.durationMinutes = durationMinutes
        self.avaliador = 0
    
    def __str__(self) -> str:
        return f"Filme: {self.name}"
    
    def techinal_sheet(self):
        print("##Dados do Filme##")
        print(f"Nome do filme: {self.name}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Esta no Plano?: {self.includedPlan}")
        print(f"Avaliação do Filme: {self.avaliacaoTo}")
        print(f"Duração do Filme: {self.durationMinutes}\n")
        print(f"Total Avaliadores: {self.avaliador}\n")
    
    def avaliacao(self, note):
        self.avaliacaoTo += note
        self.avaliador += 1
    
    def media(self):
        print(f"Média do Filme: {self.name} é: {self.avaliacaoTo / self.avaliador}")
    
mdm = Movie("Madrugada dos Mortos", 2004, False, 140)
avatar = Movie("Avatar", 2023, False, 180)
avb = Movie("A Vida é Bela", 199, False, 157 )
mdm.avaliacao(8.5)
mdm.avaliacao(9)
avatar.avaliacao(9)
avatar.avaliacao(7)
mdm.techinal_sheet()
mdm.media()
avatar.techinal_sheet()
avatar.media()
avb.avaliacao(9.7)
avb.avaliacao(8)
avb.avaliacao(6)
avb.techinal_sheet()
avb.media()