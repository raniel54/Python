gameName = "Fifa 24"
gameDescription = """
Fifa é um jogo de futebol, desenvolvido pela EA Sports,
que possibilita jogar localmente ou online
"""

print(gameName.upper()) # Retornar string em maiúsculo
print(gameName.lower()) # Retornar string em minusculo
print(gameName.capitalize())# Apenas a primeira letra em maiúsculo
print(gameName.title()) # Apenas a primeira letra em maúsculo
print(gameName.center(10, '-')) # Retorna a string centralizada com caractere de preenchimento
print(gameName.find("i")) # Retorna a posição de um determinado caractere
print(gameDescription.count("F")) #Conta caracteres
print(gameDescription.count("a")) #Conta caracteres
print(gameDescription.replace("Fifa", "Pes")) # altera um elemento por outro
print(gameDescription.split(','))
