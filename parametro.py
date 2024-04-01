class game:
    def __init__(self, name, lancamento, genero, descricao ) -> None:
        self.name = name
        self.lancamento = lancamento
        self.duracao = genero
        self.descricao = descricao
        
    def __str__(self) -> str:
        return f"Game: {self.name}"
Game = game ("Diablo 4", 2023, "Dungeon crawler", "A batalha interminável entre o Paraíso Celestial e o Inferno Ardente continua e o caos ameaça consumir Santuário. Com inúmeros demônios para matar")
print(Game)