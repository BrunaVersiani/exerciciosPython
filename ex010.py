real = float(input('Digite uma quantia em reais, para converter:  '))
dolar = 5.19*1
euro = 5.33*1
print('Com {:.2f} R$ você consegue comprar {:.2f} Dolares. '.format(real, (real/dolar)))
print('Com {:.2f} R$ você consegue comprar {:.2f} Euros. '.format(real, (real/euro)))
