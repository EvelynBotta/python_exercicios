print('Bom-dia, aqui vamos te ajudar a calcular a Tensão, Resistência e Corrente\n')
print('1. tensão(em volt)\n')
print('2. resistência(em ohm)\n')
print('3. corrente\n')
valor=(input('Qual grandeza deseja calcular: (1,2 ou 3) '))
if valor=='1':
    resistencia=float(input('Mostre o valor da resistência:'))
    corrente=float(input('Apresente a corrente:'))
    resultado=resistencia*corrente
    print(f'A tensão é de: {resultado}')
elif valor=='2':
    tensao=float(input('Mostre o valor da tensão:'))
    corrente=float(input('Apresente a corrente:'))
    resultado2=tensao/corrente
    print(f'A resistência é de: {resultado2}')
elif valor=='3':
     tensao=float(input('Mostre o valor da tensão: '))
     resistencia=float(input('Apresente a resistência'))
     resultado3=tensao/resistencia
     print(f'A corrente é de: {resultado3}')
else:
    print('O valor inserido está incorreto')


