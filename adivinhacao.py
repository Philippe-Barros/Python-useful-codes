from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
resultado = randint(0, 5)  # necessário para sortear
adivinhacao = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(3)  # segundos para o delay
if adivinhacao == resultado:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(resultado, adivinhacao))