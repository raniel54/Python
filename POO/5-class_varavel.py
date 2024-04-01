class Movie:
    plataforma = "HBO MAX"
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
        print(f"Plataforma: {Movie.plataforma}")
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
        print(f"Média do Filme: {self.name} é: {self.avaliacaoTo / self.avaliador}\n")
    
mdm = Movie("Madrugada dos Mortos", 2004, False, 140)
avatar = Movie("Avatar", 2023, False, 180)
avb = Movie("A Vida é Bela", 199, False, 157 )
mdm.avaliacao(8.5)
mdm.avaliacao(9)
mdm.techinal_sheet()
mdm.media()
# Modificando a plataforma
Movie.plataforma = "Star +"
avatar.avaliacao(9)
avatar.avaliacao(7)
avatar.techinal_sheet()
avatar.media()
# Modficando a plataforma
Movie.plataforma = "Netflix"
avb.avaliacao(9.7)
avb.avaliacao(8)
avb.avaliacao(6)
avb.techinal_sheet()
avb.media()