nome = 'Evelyn'
tentativa = 3
senha = 123456
while tentativa > 0:
    teste=int(input('Digite sua senha: '))
    if teste != senha:
        tentativa -=1
        if tentativa==0:
            print('A sua senha foi bloqueada, por favor, dirija-se a um de nossos caixas.')
            break
        print(f'Senha Incorreta. Você tem mais {tentativa} tentativas.')
    else:
        print('Senha Correta')
        print(f'Olá,{nome}. Seja bem vindo(a) ao banco')
        break