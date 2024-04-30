name = input("Digite o seu nome:\n")
"""
-Arquivos:
1 - opção W - escrita
2 - opção a - acrescentar
3 - opção r - escrever
"""
# # Alternativa 1
# file = open("name.txt", "a")
# file.write(f"{name}\n")
# file.close()

# Alternativa 2

with open("name.txt", "a") as file:
          file.write(f"{name}\n")


