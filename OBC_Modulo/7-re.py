import re

text = 'OneBitCode: Transformamos pessoas em programadores sem limites'
# 1 - Indice incial e final de palavra

# O r significa que estamos trabalhando com uma string bruta (raw string)
match = re.search(r'pessoas em programadores', text)
print('Índice incial ', match.start())
print('Indice final ', match.end())

# 2 - Buscando o indice que possui o ponto

site = 'https://google.com'
match = re.search(r'\.', site)
print(match)

# 3 - Buscando uma lista de caracteres dentro de uma frase

padrao = '[a-m]'
result = re.findall(padrao, text)
print(text)
print(result)

# 4 - Verificando o inciio de uma string

rule = r'^A'
frases = ['A casa está suja', 'O dia está lindo', 'Vamos passear']
for f in frases:
    if re.match(rule, f):
        print(f'Corresponde: {f}')
    else:
        print(f"Nao corresponde: {f}")
        
# 5 - Verificando o final de uma string
rule_end = r'!$'
frase2  = 'O dia está lindo'
match = re.search(rule_end, frase2)
if match:
    print("Sim, corresponde")
else:
    print("Não corresponde")