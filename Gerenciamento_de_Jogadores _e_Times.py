# ## Gerenciamento de Jogadores e Times

# #Escreva um programa em python que realize o gerenciamento de jogadores. Ele deve atender aos seguintes requisitos:

# #- Adicionar um time
# #- Remover um time
# #- Listar times
# #- Adicionar jogador em um time
# #- Remover jogador de um time
# #- Listar jogadores de um time
# 1. A opção de listar os times deve mostrar o índice, o nome e a quantidade de jogadores do time.
# 2. A opção de adicionar um time deve pedir um nome para o time que será cadastrado.
# 3. A opção de remover um time deve pedir o índice específico do time que foi cadastrado para fazer a sua exclusão.
# 4. A opção de adicionar um jogador em um time deve pedir um índice do time que foi cadastrado e associar com o nome do jogador que será adicionado.
# 5. A opção de remover um jogador em um time deve pedir um índice do time que foi cadastrado e utilizar esse índice para remover o jogador que fora cadastrado no time.
# 6. A opção de listar os jogadores de um time deve ser informado o índice de um time e listar os jogadores que foram associados a ele.

# Este é o exercício de revisão do módulo, então aproveite para utilizar todos os recursos vistos até agora, como os funções, condições, loop, listas, etc.

teams = {}
done = False

while not done:
    # Opção no programa
    print("O que voce deseja fazer?")
    print("1. Adicionar um time")
    print("2. Remover um time")
    print("3. Listar times")
    print("4. Adicionar jogador em um time")
    print("5. Remover jogador de um time")
    print("6. Listar jogadores de um time")
    print("7. Sair")
    
    choice = input (">")
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        pass
    elif choice == "6":
        pass
    elif choice == "7":
        done = True
    else:
        print("Opção invalida")
    