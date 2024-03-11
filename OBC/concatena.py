name = input("Digite o nome do jogo\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo\n"))
gamePrice = float(input("Digite o preço do jogo\n"))
planincluded = bool(input("Esta incluido no plano?\n"))


#Alternativa 1
#print("###Dados do Jogo###")
#print("===================")
#print("Nome do jogo:", name, "\nAno de lançamento:", yearLaunch, "\nPreço do jogo:", gamePrice, 
#      "\nEstá incluido no plano?:", planincluded)

#Alternativa2
print(f"Nome do jogo:{name} \nAno do Lançamento: {yearLaunch} \nPreço do Jogo: {gamePrice} \nEstá incluido no plano? {planincluded}" )