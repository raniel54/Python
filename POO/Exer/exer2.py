# ## Classe Produto e método desconto

# Desenvolva uma classe em Python para atender as seguintes especificidades de um Produto:

# 1. Cada produto deve ter um preço e um nome.
# 2. A classe deve ter um método construtor e o método dundle str.
# 3. A classe deve ter um método para desconto. O método deve receber o desconto em percentual e realizar o cálculo de quanto ficaria o preço final com o desconto.

class produto:
    def __init__(self, name, sabor, ml) -> None:
        self.name = name
        self.valor = 9.5
        self.sabor = sabor
        self.ml = ml
        self.dp = 0
        self.desconto = 0
        

    def __str__(self) -> str:
        return f"Produto: {self.name}"
    
    def informacoes(self):
        print("##Informações do Produto##")
        print(F"Produto:{self.name}\n")
        print(F"Preço:{self.valor}\n")
        print(F"valor do desconto: {self.dp}\n")
        
    
    def des(self, nota):
        self.dp += nota
        self.desconto = self.valor * self.dp/100
        
    def media(self):
        print(f"Produto: {self.name} custa R${self.valor} é teve um desconto de {self.dp}% ficando {self.valor - self.desconto }")

monster = produto("MONSTER ENERGY JUICE PIPELINE PUNCH","Maracujá, Laranja e Goiaba", 375)
monster.des(20)
monster.media()