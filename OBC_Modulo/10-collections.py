from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Contar itens de uma lista
frutas = ["Maça", "Banana", "uva", "Pera",
          "uva", "Maça", "Laranja", "Abacaxi",
          "Tangerina", "uva", "Pera"]
print(frutas)
print(Counter(frutas))

# 2 - Utilizando tupla nomeada
game = namedtuple('game', ['name', 'price', 'nota'])
g1 = game("God of war", 99.90, 9.1)
g2 = game("Resident Evil 4", 119.90, 9.2)
print(g1)
print(g2)

# 3 - Ordenada dicionarios
estudantes = {"Raniel":27, "Rosa":42, "Zaad": 47, "janaina": 48}
a = sorted(estudantes.items(), key=itemgetter(0))
print(estudantes)
print(a)

# 4 - utilizando fila ambas extremidades
deq = deque([20, 40, 60, 80])
deq.appendleft(10)
print(deq)
deq.append(90)
deq.popleft()
deq.pop()
print(deq)