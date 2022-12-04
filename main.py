a = input('Digite um termo: ')
b = input('Digite o segundo termo: ')
operacao = input('Digite uma operação (+,-,*,/) a ser feita:')
if operacao == '+':
  soma = int(a) + int(b)
  print(soma)

if  operacao == '-':
  subtracao = int(a) - int(b)
  print(subtracao)

if operacao == '*' :
  multiplicacao = float(a) * float(b)
  print(multiplicacao)

if operacao == '/' :
  divisao = float(a) / float(b)
  print(divisao)

else:
  print('Erro, operaçao invalida')
  
  