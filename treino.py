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
        n1 = float(input('Digite o primeiro numero: '))
        n2 = float(input('Digite o segundo numero: '))
        print('O resultado é:',n1 + n2)

    elif opcao == '2':
        n1 = float(input('Digite o primeiro numero: '))
        n2 = float(input('Digite o segundo numero: '))
        print('O resultado é:',n1 - n2)

    elif opcao == '3':
        n1 = float(input('Digite o primeiro numero: '))
        n2 = float(input('Digite o segundo numero: '))
        print('O resultado é:',n1 * n2)

    elif opcao == '4':
        n1 = float(input('Digite o primeiro numero: '))
        n2 = float(input('Digite o segundo numero: '))
        if n2 == 0:
            print('Error...')
        else:
            print('O resultado é:', n1 / n2)

    elif opcao == '5':
        print('Encerrando...')
        break
    else:
        print('Error')