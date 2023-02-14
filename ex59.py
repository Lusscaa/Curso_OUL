n1 = int(input("Digite um numero: "))
n2 = int(input("Digete outro numero: "))
op = 0
while op != 5:
    print('''
            [1] SOMAR
            [2] MULTIPLICAR
            [3] MAIOR  
            [4] NewNumber   
            [5] QUIT ''')
    op = int(input("Sua opção"))
    if op == 1:
        r = n1 + n2
        print("Resultado é {}".format(r))
    elif op == 2:
        r2 = n1 * n2
        print('Resultado é {}'.format(r2))
    elif op == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("Resultado é {}".format(maior))

    elif op == 4:
        n1 = int(input("Digite um numero"))
        n2 = int(input("Digite outro numero"))

    elif op == 5:
        print("Finalizando...")

    else:
        print('Opção invalida tente novamente')
    print('=-=' * 10)

print('FIM...')
