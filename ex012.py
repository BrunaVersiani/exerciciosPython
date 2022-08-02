preço = float(input('Digite o valor do produto: R$'))
desconto = preço*5/100
print('O preco deste produto é R$ {:.2f}, com 5% de desconto ficará R$ {:.2f}. '.format(preço, preço-desconto))
