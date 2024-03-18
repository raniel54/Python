gameName = input("digite o nome do jogo\n")
qtdRating = 0
totalRating = 0
rating = 0
average  = 0

while(rating != -1):
    rating  = float(input("Informe a nota do jogo\n"))
    if(rating != -1):
        totalRating += rating # totalRating = totalRating + rating
        qtdRating += 1 #qtdRating = qtdRating +1
        average = totalRating / qtdRating
print(f"Media das avaliacoes do jogo {gameName} e {average:.2f}")