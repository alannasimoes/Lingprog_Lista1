def calculos():
    x = int(input('Digite o primeiro número inteiro: '))
    y = int(input('Digite o segundo número inteiro: '))
    z = input('Digite um número real: ')
    z = z.replace(',', '.') #Caso o separador decimal seja ',', troca por '.'
    z = float(z)
    print('Cálculo a:')
    print('O produto do dobro do primeiro com metade do segundo:', end=' ')
    print(f'{(2*x)*(y/2)}\n')
    
    print('Cálculo b:')
    print('A soma do triplo do primeiro com o terceiro:', end=' ')
    print(f'{(3*x)+z}\n')
    
    print('Cálculo c:')
    print('O terceiro elevado ao cubo:', end=' ')
    print(f'{z**3}')
    
calculos()