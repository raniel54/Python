class Movie:
    def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes
    
    def __str__(self) -> str:
        return f"Filme: {self.name}"
    #def __str__(self) -> str:
        return f"Ano de Lançamento: {self.yearLaunch}"#
        
        
movie = Movie("Madame Teia",2024, False, 5.9, 118 )
movie2 = Movie("Godzilla e Kong: O Novo Império ", 2024, False, 8.2, 125 )
print(movie)
print(movie2)

        