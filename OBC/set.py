gameSet = {"Fifa24", "Red Dead 2", "Star wars", "Batman Arkan knight", 
              "Call of duty", "Resident Evil 4"}

print(gameSet)

# 1 - Buscar o tamnho do set

print(len(gameSet))

# 2 - True e 1 são considerados o mesmo valor
exampleSet = {"Fifa24", True, 1 , 90.50}

# 3 - Adicionar item de outro set
gameSet.update(exampleSet)
print(gameSet)

# 4 - Remover um item no set
gameSet.remove(True)
gameSet.remove(90.50)
print(gameSet)

# - Nao possibilita recuperar valores via fatiamento ou slice