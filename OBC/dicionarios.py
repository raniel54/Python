gameFifa = {
    "name": "Fifa 23",
    "yearLaunch": 2024,
    "gamePrice": 90.50,
    "classification": 8.5,
    "genre": ["esporte", "familia"]
}

print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

# 1 - Recuperar um elemento do dicionário
print(gameFifa['genre'])
print(gameFifa.get('classification'))

# 2 - Buscar apenas as chaves do dicionário
print(gameFifa.keys())

# 3 - Bsucar apenas os valores do dicionário
print(gameFifa.values())

# 4 - Buscar itens do docion´~ario com chave e valor
print(gameFifa.items())

# 5 - Adicionar itens no dicionário
gameFifa["players"] = 2
print(gameFifa)

# 6 - Atualizar itens no dicionario
gameFifa.update({"players": 1})
print(gameFifa)

# 7 - Remover item no dicionário
gameFifa.pop("players")
print(gameFifa)