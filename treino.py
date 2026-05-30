while True:
    print('===Cauculadora===')
    print('''
    Escolha uma opção:
    1-soma
    2-subtrair
    3-multiplicar
    4-dividir
    5-Sair   
    ''')

    opcao = input('Escolha uma opção:')
    if opcao == '1':
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
        print('O resultado é:',n1 + n2)

    if opcao == '2':
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
        print('O resultado é:',n1 - n2)

    if opcao == '3':
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
        print('O resultado é:',n1 * n2)

    if opcao == '4':
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
        print('O resultado é:',n1 / n2)

    elif opcao == '5':
        print('Encerrando...')
        break
    else:
        print('Error')