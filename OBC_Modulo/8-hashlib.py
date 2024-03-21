import hashlib

#1 - verificar os algoritmos disponiveis
print(hashlib.algorithms_available)

# 2 - Algoritmos disponiveis de acordo com o SO

print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o SHa256

algorithm = hashlib.sha256()
print(algorithm.digest)
message = "A Melhor forma de prever o futuro é criá-lo".encode()
algorithm.update(message)
print(algorithm.hexdigest())

# 4 - Utilizando o MD5

md5 = hask