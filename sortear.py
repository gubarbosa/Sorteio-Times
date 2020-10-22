import random
import colored


jogadores = ['Gustavo', 'Pedro', 'Lucas', 'Zimmerman', 'Arthur', 'Wanderli', 'Patrick', 'Jonas', 'Nazo', 'Nicolas', 'Wesley', 'Adriano', 'Luan', 'Matheus', 'Junior', 'Andrei', 'Renato', 'Dalton']
camisa_branca = []
camisa_preta = []
camisa_branca = random.sample(jogadores, k=9)
for x in camisa_branca:
    for y in jogadores:
        if x == y:
            jogadores.remove(x)

camisa_preta = random.sample(jogadores , k=9)


print(camisa_branca)    
print(camisa_preta)

