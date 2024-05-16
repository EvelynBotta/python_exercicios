variavel= int(input('Insira a quantidade de números que deseja calcular a média: '))
soma = 0
iteracao = 1
while iteracao<=variavel:
    n=float(input(f'Agora digite o {iteracao}° número: '))
    soma += n
    iteracao += 1
print(f'A média é de: {soma/variavel} ')

