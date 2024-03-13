gameName = "Fifa 24"
gameDescription = """
Fifa é um jogo de futebol desenvolvido pela EA Sports
e que possibilita jogar localmente ou online
"""

# string[início:fim] - indice começa na posição 0 / indice final -1

#1 - Buscar toda string a partir da primeira posição

print(gameName[0:])

#2 - Buscar toda string até a última posição

print(gameName[:7])

#3 - buscar toda string da terceira até a última posição

print(gameName[2])

"""string[início:fim] - indice começa na posição 0 / indice final -1
    passo - determina o incremento. Por Padrão esse número é o 1.
"""
# 4 - bucar toda a string de 2 em 2 caracteres
print(gameName[::2])

# 5 - buscar toda a string nos indices ímpares
print(gameName[1::2])

# 6 - Inverter uma string de trás pra frente
print(gameName[::-1])