# 1 - Função de potência de número
power = lambda num: num **2

# 2 - Função que verifica se o número é par
pair = lambda x: x % 2 ==0

# 3 - Funação que divide um número por outro
divnum = lambda x, y : x /y

# 4 - Função que inverte uma string
reverse = lambda s: s[::-1]

print(power(5))
print(power(9))
print(pair(27))
print(pair(30))
print(divnum(10, 2))
print(divnum(6, 2))
print(reverse("Python"))
print(reverse("Javascript"))

