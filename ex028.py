''' Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''
from random import randint
from time import sleep
computador = randint(0, 5) #Computador pensa
print('-*-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar qual...')
print('-*-' * 20)
jogador = int(input('Em que número pensei? ')) #Jogador adivinha o número
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Você conseguiu vencer!')
else:
    print('Você perdeu. Pensei no número {} e não no {}! '.format(computador, jogador))

