# Escreva um programa que leia um número e represente o número antecessor e sucessor desse número que foi lido, 
# utilizando operadores de atribuição

num1 = int(input("Digite um número\n"))

ante = num1 - 1
suce = num1 + 2

print(f"O numero escolhido foi {num1} é o número antecessor a ele é {ante} e o seu sucessor é {suce}")


# Escreva um programa que leia quatro números e calcule a média entre esses números
nota1 = int(input("Digite o valor da nota\n"))
nota2 = int(input("Digite o valor da nota\n"))
nota3 = int(input("Digite o valor da nota\n"))
nota4 = int(input("Digite o valor da nota\n"))

nota5 = nota1 + nota2 + nota3 + nota4 / 4

print(f"As notas foram {nota1}, {nota2}, {nota3}, {nota4} e a media foi de {nota5}")
