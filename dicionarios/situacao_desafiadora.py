produtos = {}
interacao = 0 
while True:
    interacao += 1 
    produto=(input(f'Insira o {interacao}° produto: '))
    valor_uni=float(input(f'Qual o valor do produto?: '))
    quantidade_item=int(input(f'Quantos você deseja comprar?: '))
    produtos.update({interacao:[produto, valor_uni, quantidade_item]})

    loop=(input('Você deseja adicionar mais algum item?(S/N)'))
    if loop.upper()=='N':
        break
    
total=0

print(50 * '-')
print('Carrinho de Compras')
print(50 * '-')

for interacao, produto in produtos.items():
    subtotal = produto[1] * produto[2]
    print(f'{produto[0]} - R$ {produto[1]:2f} - {produto[2]} un - R$ {subtotal:.2f}')
    total += subtotal

print(50 * '-')
print(f'Total da Compra: R$ {total:.2f}')
print(50 * '-')
       
  

    