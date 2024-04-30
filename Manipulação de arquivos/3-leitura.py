name = []

with open("Manipulação de arquivos/name.txt", "r", encoding="utf-8") as file:
    for line in file:
        name.append(line.rstrip())
for name in sorted(name):
    print(f"Ola, {name}")