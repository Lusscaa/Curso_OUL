from random import randint
c = randint(0, 10)
print('Pensei em um numero vamos ver se voce sabe qual é')
acertou = False
p = 0
while not acertou:
    jogador = int(input("Qual é seu palpite?"))
    p += 1
    if jogador == c:
        acertou = True
print('Parabens voce acertou com {}'.format(p))
