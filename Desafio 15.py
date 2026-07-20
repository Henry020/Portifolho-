tempo = int(input('Quanto tempo ficou alugado?'))
km = float(input('Qual a quantidade de km rodados?'))
pago = (tempo * 60) * (km * 0.15 )
print('O total a pagar é de R${:.2f}'.format(pago))