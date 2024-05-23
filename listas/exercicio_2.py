numeros = []
print('Digite 5 números inteiros: ')
for x in range (5):
    numero = int (input(f'Digite o {x+1}° número inteiro: '))
    numeros.append(numero)
print(f'Lista de números:', numeros)
soma = sum(numeros)
maior = max(numeros)
menor = min(numeros)
media = soma / len(numeros)
print(f'Soma de todos:', soma)
print(f'Maior número:', maior)
print(f'Menor número:', menor)
print(f'A média entre eles é:', media)
