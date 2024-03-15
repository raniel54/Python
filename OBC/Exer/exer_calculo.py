#Cálculo da Distância

# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.Calcule o preço da passagem, 
# cobrando R$ 0,50 por km para viagens de até de 200 km, e R$0,35 para viagens mais longas. utilizando operadores de atribuição

km = float(input("Digite que deseja percorrer em km\n")) 

if km <= 200:
    calcule = km * 0.50
else:
    calcule = km * 0.35
print(f"O KM desejado é {km:.1f} o preço da passagem é {calcule:.2f}") 

## Aumento salário funcionário

#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

sal = float(input("Digite o seu salario\n"))
au = sal * 0.10
inf = sal * 0.15

if sal > 1.250:
    cal = sal + au
else:
    cal = sal + inf
print(f"Seu salario é {sal:.1f} com o aumento foi para {cal}")

    
