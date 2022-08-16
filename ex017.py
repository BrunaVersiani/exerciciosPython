import math
co = float(input('O comprimento do cateto oposto: '))
ca = float(input('O comprimento do cateto adjacente'))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2}'.format(hi))


#Dessa maneira não precisa fazer importação de bibliotecas
'''
co = float(input('O comprimento do cateto oposto: '))
ca = float(input(' O comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) meio que calcula a raiz quadrada ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''


