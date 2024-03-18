"""
*args  =  Utilizamos ele quando não temos certeza de quantos argumentos
queremos ter em uma função.
- Os argumentos são passados como uma tupla

**Kwargs - AL = em dos valores podemos passar também as respectivas
chaves para cada argumento.
- Os arquimentos são passados como um dicioário

"""

# 1 - Soma de números
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n # sum_total = sum_total + n
    print(f"Soma é: {sum_total}")
    
sum(7)
sum(7,9)
sum(7, 9, 10, 11)
sum(7, 10, 9, 8, 7, 6)

# 2 - Apresentação de cursos

def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")
presentation(name = "Python", category = "Backend", Level="Iniciante")
presentation(name = "Visão Computacional Python", category = "IA", Level="Avançado")
presentation(name = "Dashboards com Dash", category = "Data science", Level="Intermediário")