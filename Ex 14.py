def pesoPeixe():
    peso = input('Digite o peso de peixes: ')
    peso = peso.replace(',', '.')
    peso = float(peso)
    excesso = peso - 50
    if excesso > 0:
        multa = excesso*4
        print(f'Multa no valor de R${round(multa,2)}')
    else:
        print('Peso dentro do permitido, não há multa')

pesoPeixe()