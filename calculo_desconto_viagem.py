valor_bruto = float(input('Informe o valor do pacote: '))

print('Selecione a categoria')
print('1 - Econômica')
print('2 - Executiva')
print('3 - Primeira Classe')
categoria = int(input('Informe o número:  '))


if categoria == 1:
    n_viajantes = int(input('Quantidade de viajantes: '))
    if n_viajantes == 1:
        print(f'Valor da compra: {valor_bruto}')

    elif n_viajantes == 2:
        desconto = valor_bruto * 0.03
        liquido = valor_bruto * 0.97
        medio = float(liquido / n_viajantes)
        print(f'Valor bruto: {valor_bruto}')
        print(f'Desconto: {desconto}')
        print(f'Valor líquido: {liquido}')
        print(f'Valor por viajante: {medio}')

    elif n_viajantes == 3:
        desconto = valor_bruto * 0.04
        liquido = valor_bruto * 0.96
        medio = float(liquido / n_viajantes)
        print(f'Valor bruto: {valor_bruto}')
        print(f'Desconto: {desconto}')
        print(f'Valor líquido: {liquido}')
        print(f'Valor por viajante: {medio}')

    elif n_viajantes >= 4:
        desconto = valor_bruto * 0.05
        liquido = valor_bruto * 0.95
        medio = float(liquido / n_viajantes)
        print(f'Valor bruto: {valor_bruto}')
        print(f'Desconto: {desconto}')
        print(f'Valor líquido: {liquido}')
        print(f'Valor por viajante: {medio}')

elif categoria == 2:
    n_viajantes = int(input('Quantidade de viajantes: '))
    if n_viajantes == 1:
        print(f'Valor da compra: {valor_bruto}')

    elif n_viajantes == 2:
        desconto = valor_bruto * 0.05
        liquido = valor_bruto * 0.95
        medio = float(liquido / n_viajantes)
        print(f'Valor bruto: {valor_bruto}')
        print(f'Desconto: {desconto}')
        print(f'Valor líquido: {liquido}')
        print(f'Valor por viajante: {medio}')

    elif n_viajantes == 3:
        desconto = valor_bruto * 0.07
        liquido = valor_bruto * 0.93
        medio = float(liquido / n_viajantes)
        print(f'Valor bruto: {valor_bruto}')
        print(f'Desconto: {desconto}')
        print(f'Valor líquido: {liquido}')
        print(f'Valor por viajante: {medio}')

    elif n_viajantes >= 4:
        desconto = valor_bruto * 0.08
        liquido = valor_bruto * 0.92
        medio = float(liquido / n_viajantes)
        print(f'Valor bruto: {valor_bruto}')
        print(f'Desconto: {desconto}')
        print(f'Valor líquido: {liquido}')
        print(f'Valor por viajante: {medio}')



elif categoria == 3:
    n_viajantes = int(input('Quantidade de viajantes: '))
    if n_viajantes == 1:
        print(f'Valor da compra: {valor_bruto}')

    elif n_viajantes == 2:
        desconto = valor_bruto * 0.10
        liquido = valor_bruto * 0.90
        medio = float(liquido / n_viajantes)
        print(f'Valor bruto: {valor_bruto}')
        print(f'Desconto: {desconto}')
        print(f'Valor líquido: {liquido}')
        print(f'Valor por viajante: {medio}')

    elif n_viajantes == 3:
        desconto = valor_bruto * 0.15
        liquido = valor_bruto * 0.85
        medio = float(liquido / n_viajantes)
        print(f'Valor bruto: {valor_bruto}')
        print(f'Desconto: {desconto}')
        print(f'Valor líquido: {liquido}')
        print(f'Valor por viajante: {medio}')

    elif n_viajantes >= 4:
        desconto = valor_bruto * 0.20
        liquido = valor_bruto * 0.80
        medio = float(liquido / n_viajantes)
        print(f'Valor bruto: {valor_bruto}')
        print(f'Desconto: {desconto}')
        print(f'Valor líquido: {liquido}')
        print(f'Valor por viajante: {medio}')
else:
    print('Categoria não existente, digite uma categoria válida')