"""
-Arquivos:
1 - opção W - escrita
2 - opção a - acrescentar
3 - opção r - escrever
"""
with open("name.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(f"{line.rstrip()}")