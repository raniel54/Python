class Animal:
    name = ""
    size = ""
    color = ""
    
    def eat(self):
        print("Animal se alimentando")
        
        
class Horse(Animal):
    race = ""
    
    def escape(self):
        print("cavalo fugindo")
        
class Leao(Animal):
    mjuba = True
    
    def hunt(self):
        print("Leao caçando")

h = Horse()
h.name = "Trident"
h.color = "Branco"
h.escape()
h.eat()

l = Leao()
l.name = "Senses"
l.color = "Marrom"
l.hunt()
l.eat()