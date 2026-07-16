produto = float(input('Digite o valor do produto: R$'))
desconto = float(input("Digite o valor do desconto: "))
valor = produto - (produto * desconto/100)
print('Um produto de R${} com desconto de {}% fica no valor de R${}'.format(produto, desconto, valor))

#===========================================================================================
#programa para calcular porcentagem !