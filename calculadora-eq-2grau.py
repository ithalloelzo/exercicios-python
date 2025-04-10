import math #Pra poder calcular a raiz

#Solicitar os valores de a, b, c
a = float(input('Informe o valor de A: '))
b = float(input('Informe o valor de B: '))
c = float(input('Informe o valor de C: '))

#Calculo de delta
delta = b ** 2 - 4 * a * c

#Regras do delta
if delta >0.0:
    #Existem duas possíveis soluções
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    print(f'Os valores de x que satisfazem a equação são {x1} e {x2}')
elif delta == 0.0:
     #Existe apenas uma solução possível/pode ser + ou -
     x1 = (-b + math.sqrt(delta)) / (2 * a)
     print(f'O valor x que satifaz a equação é {x1} ')

elif delta <0.0:
     print(f'Não existem valores reais para o x da equação: {a}x²+{b}-{c}')