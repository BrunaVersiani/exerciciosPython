lar = float(input('Qual a largura de sua parede? '))
alt = float(input('Qual a altura da sua parede? '))
area = lar * alt
print('Sua parede tem as dimenções de {} x {} e sua area e de {} metros.'.format(lar, alt, area))
tinta = area/2
print('Para pintar essa parede, voce precisará de {} litros de tinta.'.format(tinta))
