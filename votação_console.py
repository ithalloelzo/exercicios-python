#Digitar o voto de cada membro(5)
#Informar qual console foi escolhido

print('Escolha seu prêmio: Playstation, Xbox ou Nintendo')
voto1 = input('Informe seu voto: ')
voto2 = input('Informe seu voto: ')
voto3 = input('Informe seu voto: ')
voto4 = input('Informe seu voto: ')
voto5 = input('Informe seu voto: ')

playstation = 0
xbox = 0
nintendo = 0

if voto1.lower() == 'playstation':
    playstation = playstation + 1

elif voto1.lower() == 'xbox':
    xbox = xbox + 1

elif voto1.lower() == 'nintendo':
    nintendo = nintendo + 1
else:
    print("O colaborador 1, digitou um console inexistente")

if voto2.lower() == 'playstation':
    playstation = playstation + 1

elif voto2.lower() == 'xbox':
    xbox = xbox + 1

elif voto2.lower() == 'nintendo':
    nintendo = nintendo + 1
else:
    print("O colaborador 2, digitou um console inexistente")

if voto3.lower() == 'playstation':
    playstation = playstation + 1

elif voto3.lower() == 'xbox':
    xbox = xbox + 1

elif voto3.lower() == 'nintendo':
    nintendo = nintendo + 1
else:
    print("O colaborador 3, digitou um console inexistente")

if voto4.lower() == 'playstation':
    playstation = playstation + 1

elif voto4.lower() == 'xbox':
    xbox = xbox + 1

elif voto4.lower() == 'nintendo':
    nintendo = nintendo + 1
else:
    print("O colaborador 4, digitou um console inexistente")

if voto5.lower() == 'playstation':
    playstation = playstation + 1

elif voto5.lower() == 'xbox':
    xbox = xbox + 1

elif voto5.lower() == 'nintendo':
    nintendo = nintendo + 1
else:
    print("O colaborador 5, digitou um console inexistente")

if playstation > xbox and playstation > nintendo:
    print('O console escolhido foi o playstation ')
elif xbox > playstation and xbox > nintendo:
    print('o console escolhido foi o xbox')
elif nintendo > playstation and nintendo > xbox:
    print('O console escolhido foi o nintendo')
else:
    print('Houve um empate, favor entrar em contato com o responsavel')









