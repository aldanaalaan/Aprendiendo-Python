# Ciclo While

num1 = int(input('Dime hasta que numero quieres la sucecion de 5 en 5: '))

# Variables
i = 0
cad1 = ''

while i <= num1:
    cad1 += str(i) + ', '
    i += 5

print(cad1)
