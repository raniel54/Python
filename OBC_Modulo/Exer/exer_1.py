from Modulo import strings

name = input("Digite uma frase\n")
# ## Módulo de strings

# Escreva um módulo em python para tratar algumas strings e que possua as seguintes funcionalidades:

# 1. Inverter uma string de trás pra frente.
print(strings.invertida(name))

# 2. Retornar apenas letras com índice par.
print(strings.even_characters(name))

# 3. Retornar apenas letras com índice ímpar.
print(strings.odd_characters(name))


