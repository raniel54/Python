# Escreva um programa que leia um número e represente o número antecessor e sucessor desse número que foi lido, 
# utilizando operadores de atribuição

num1 = int(input("Digite um número\n"))

print(f"O numero escolhido foi {num1} é o número antecessor a ele é {num1 -1} e o seu sucessor é {num1 + 1}")


# Escreva um programa que leia quatro números e calcule a média entre esses números
nota1 = float(input("Digite o valor da primeira nota\n"))
nota2 = float(input("Digite o valor da segunda nota\n"))
nota3 = float(input("Digite o valor da terceira nota\n"))
nota4 = float(input("Digite o valor da da quarta nota\n"))

nota5 = (nota1 + nota2 + nota3 + nota4) / 4

print(f"As notas foram {nota1}, {nota2}, {nota3}, {nota4} e a media foi de {nota5}")
