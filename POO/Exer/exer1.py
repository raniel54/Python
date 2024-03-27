## Avaliação e Média da Nota de Filmes

# Desenvolva novas funcionalidades para complementar o nosso gerenciamento da classe Filmes. Segue o escopo das funcionalidades:

# 1. Uma das funcionalidades requeridas é que o usuário possa realizar a avaliação de um filme 
# passando uma nota com parâmetro e que essa nota seja salva no atributo específico da classe.
# 2. Assim que uma avaliação for realizada, deve ser incrementado o total de avaliadores daquele filme. 
# Obs: Considere criar um atributo específico para esse fim.
# 3. Para cada filme ter uma nota de avaliação média que consiste na divisão do total de avaliação pelo total de avaliadores.

class Movie:
    def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes
    
    def __str__(self) -> str:
        return f"Filme: {self.name}"
    
    def techinal_sheet(self):
        print("##Dados do Filme##")
        print(f"Nome do filme: {self.name}")
        print(f"Ano de lançamento: {self.yearLaunch}")
        print(f"Esta no Plano?: {self.includedPlan}")
        print(f"Avaliação do Filme: {self.note}")
        print(f"Duração do Filme: {self.durationMinutes}\n")
        
godekon = Movie("Godzilla e Kong: O Novo Império", 2024, False, 8.2, 115)
kufupa = Movie("Kung Fu Panda 4", 2024, True, 7.0, 94)

godekon.techinal_sheet()
kufupa.techinal_sheet()