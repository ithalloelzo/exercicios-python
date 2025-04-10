idade = int(input('Informe sua idade: '))

if idade <= 2:
    n_bpm = int(input('Informe o seu bpm: '))
    if n_bpm >=120 and n_bpm <=140:
        print('Batimentos dentro da faixa recomendada')
    elif n_bpm <120:
        print('Batimentos abaixo da faixa recomendada')
    elif n_bpm >140:
        print('Batimentos acima da faixa recomendada')

if idade >=8 and idade <=17:
    n_bpm = int(input('Informe o seu bpm: '))
    if n_bpm >=80 and n_bpm <=100:
        print('Batimentos dentro da faixa recomendada')
    elif n_bpm <80:
        print('Batimentos abaixo da faixa recomendada')
    elif n_bpm >100:
        print('Batimentos acima da faixa recomendada')

if idade >=18 and idade <=59:
    n_bpm = int(input('Informe o seu bpm: '))
    if n_bpm >=70 and n_bpm <=80:
        print('Batimentos dentro da faixa recomendada')
    elif n_bpm <70:
        print('Batimentos abaixo da faixa recomendada')
    elif n_bpm >80:
        print('Batimentos acima da faixa recomendada')

if idade >=60 and idade <=76:
    n_bpm = int(input('Infome o seu bpm: '))
    if n_bpm >= 50 and n_bpm <=60:
        print('Batimentos dentro da faixa recomendada')
    elif n_bpm <50:
        print('Batimentos abaixo da faixa recomendada')
    elif n_bpm >60:
        print('Batimentos acima da faixa recomendada')

    








