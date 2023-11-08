nome = input('Digite seu nome')
alt = float(input('digite sua altura'))
peso = float(input('digite seu peso'))
imc = peso / alt ** 2
print('{} Tem {}m de altura, \npesa {}Kg e seu IMC é \n{}'.format(nome, alt, peso, imc ))