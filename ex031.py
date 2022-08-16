'''Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''
distancia = float(input('Qual é a Distancia de sua viagem? '))
if distancia <= 200:
    preço = distancia * 0.50
    print('E o preço de sua passagem é de RS {:.2f} para uma viagem com {} km de distância. '.format(preço, distancia))
else:
    preço = distancia * 0.45
    print('E o preço de sua passagem é de R$ {:.2f} para uma viagem com {} km de distância. '.format(preço, distancia))
