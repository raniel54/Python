name = input("Digite o nome do jogo\n")
yearlaunch = int(input("Digite o ano de lancamento do jogo\n"))
classification = float(input("Digite a nota de classificacao do jogo\n"))

if classification > 8.0 or yearlaunch > 2015:
    print(f"O jogo {name} e bom. Recomendo Joga-lo")
else:
    print(f"O jogo {name} ainda nao atingiu uma boa nota. Por isso nao recomendo.")