import math
ângulo = float(input('Digite o ângulo desejado '))
seno = math.sin(math.radians(ângulo))
print('O ângulo de {:.2f} tem o seno de {:.2f} '.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo de {:.2f} tem o cosseno de {:.2f} '.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ãngulo de {:.2f} tem a tangente de {:.2f} '.format(ângulo, tangente))
