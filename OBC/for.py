gamesList = ["Fifa", "God of war", "Red Dead 2", "Uncharted", 90.5]

# 1 - Iterando valores de uma lista
for game in gamesList:
     print(game)
     
# 2 - Quando a condição for aytndida, o loop seá encerrado

for game in gamesList:
    if game == "Red Dead 2":
        break
    print(game)
    
# 3 - Quando a condição for atendida for atendida, o loop via para a proxima iteação
for game in gamesList:
    if game == "Red Dead 2":
        continue
    print(game)
    
# 4 - Avaliação do jogo

gameName = input("Digite o nome do jogo\n")
gameRating = int(input("Digite quantas avaliações deja fazer no jogo\n"))

sum = 0
for i in range(gameRating):
    note = float(input("Digite a nota para o jogo\n"))
    sum += note # sum = sum + note
print(f"Media de avaliação do jogo {gameName} e {sum/gameRating:.2f}")

