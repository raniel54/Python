import pprint

gamesDict = {
    "Resident evil 4":{
        "yearLaunch": 2023,
        "classification": 9.8,
        "genre": ["ação", "aventura"]
        
    },
    "Call of duty":{
        "yearLaunch": 2023,
        "classification": 5.1,
        "genre": ["ação", "aventura"]
        
    },
    "Donkey Kong Country":{
        "yearLaunch": 1995,
        "classification": 9.5,
        "genre": ["aventura", "plataforma"]
        
    },
}
pp = pprint.PrettyPrinter(depth=5)
pp.pprint(gamesDict)

# 1 - Buscar informação dentro de um dicionário aninhado

print(gamesDict["Call of duty"] ["genre"])

# 2 - Adicionar novo item

gamesDict["Call of duty"] ["players"] = 1
print(gamesDict["Call of duty"])

# 3 - Excluir um dicionario

del gamesDict["Resident evil 4"]
pp.pprint(gamesDict)
