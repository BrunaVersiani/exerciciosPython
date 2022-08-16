'''Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

v = float(input('Qual a velocidade atual do carro? '))
if v > 80:
    print('MULTADO! Você ultrapassou o limtite da pista que é de 80km/h! ')
    multa = (v-80) * 7
    print('O valor da multa a pagar é de R$ {:.2f} .'.format(multa))
print('Tenha um Bom Dia! Diriga com segurança. ')
