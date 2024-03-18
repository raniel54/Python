# 1 - Crie uma função que rreceba dois argumentos:Ç o primeiro nome e o segundo nome
def full_name(fname, Lname):
    print(f"Nome completo: {fname}{Lname}")

full_name("Raniel", "Oliveira")

# 2 - crie uma função que some dois numeros via parametros

def sum(a, b):
    return a + b
print(sum(10, 50))
    
# 3 - Argumentos default numa função
def address(country="Brasil"):
    print(f"Eu moro no {country}")

address()
address("Canadá")

# 4 - Avaliação do jogo
def  reating_game(qtdRating):
    game_name = input("Digite o nome do jogo \n")
    sum = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota para o jogo\n"))
        sum = note # sum = sum + note
    print(f"Media de avaliação do jogo {game_name} é: {sum / qtdRating}")
    
    
rating = int(input("Digite quantas avaliações deseja fazer no jogo \n"))
reating_game(2)
    