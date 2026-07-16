salaria = float(input('Qual o valor do seu salario? R$'))
aumento = float(input('Qual o valor do almento um porcentagem?'))
t = salaria * aumento/100
print('O valor do seu aumento de {}% é de R${}'.format(aumento,t))
total = salaria + t
print('O valor final do seu salario será de R${}'.format(total))