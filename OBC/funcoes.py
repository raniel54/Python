# 1 - Função para imprimir Hello World
def wellcome():
    print("Hello world")
    
wellcome()

# 2 - Função para somar dois números
def sum():
    print(5 + 4)
    #return 5 + 4
sum()
#print(sum()) para chamar a função return precisa chamar o print antes

# 3 - Função para cadastrar um jogo

def create_game():
    name = input("Digite o nome do jogo\n")
    yearLaunch = int(input("Digite o ano de lançamento do jogo\n"))
    gamePrice = float(input("Digite o preço do jogo\n"))
    noteRating = float(input("Digite a nota de avalição do jogo\n"))
    
    print(F"{name} - R$ {gamePrice}")
create_game()
