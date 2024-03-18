# 1 - Liste valores de 0 a 10 que sejam menor que 4

listnumbers = [i for i in range(10) if i < 4]
print(listnumbers)

gameslist = ["Mario Odyssey", "DK Country",
             "Luigis Mansion", "kirb"]

# 2 - Jogos que possuam a letra a

newList = [x for x in gameslist if "a" in x]
print(newList)

# 3 - jogos que finalizei

gameFinished = [x for x in gameslist if x != "kirb"]
print(gameFinished)