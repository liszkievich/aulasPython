primeiro_valor = input('Digite um número: ')
segundo_valor = input('Digite um outro número: ')

if primeiro_valor == segundo_valor:
    print(f'Os números {primeiro_valor=} e {segundo_valor=} são iguais.')
elif primeiro_valor > segundo_valor:
    print(f'O número {primeiro_valor=} é maior que {segundo_valor=}.')
elif primeiro_valor < segundo_valor:
    print(f'O número {primeiro_valor=} é menor que {segundo_valor=}.')
