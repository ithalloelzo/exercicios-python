#Informar o tipo de assinatura do cliente
#O faturamento anual dele

print('Qual dessas opções corresponde a sua assinatura:\nBasic\nSilver\nGold\nPlatinum')
assinatura = input('Informe o tipo da sua assinatura: ')

if assinatura.lower() == 'basic':
    faturamento_anual = float(input('Informe seu faturamento anual: '))
    bonus = faturamento_anual * 0.30
    print(f'Valor bônus a ser pago: {bonus}')

elif assinatura.lower() == 'silver':
    faturamento_anual = float(input('Informe seu faturamento anual: '))
    bonus = faturamento_anual * 0.20
    print(f'Valor bônus a ser pago: {bonus}')

elif assinatura.lower() == 'gold':
    faturamento_anual = float(input('Informe seu faturamento anual: '))
    bonus = faturamento_anual * 0.10
    print(f'Valor bônus a ser pago: {bonus}')

elif assinatura.lower() == 'platinum':
    faturamento_anual = float(input('Informe seu faturamento anual: '))
    bonus = faturamento_anual * 0.05
    print(f'Valor bônus a ser pago: {bonus}')
else:
    print('Assinatura não existente')

