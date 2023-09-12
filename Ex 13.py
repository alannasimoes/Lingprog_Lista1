def pesoIdeal(h):
    idealHomem = round((72.7*h)-58, 2)
    idealMulher = round((62.1*h)-44.7, 2)
    print(f'Peso ideal')
    print(f'Homem: {idealHomem}kg')
    print(f'Mulher: {idealMulher}kg\n')
    
pesoIdeal(1.5)
pesoIdeal(1.69)
pesoIdeal(1.81)