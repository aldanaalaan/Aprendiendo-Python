# Determinar si un numero es par o impar

# Pedir numero
num = int(input('Dame un numero: '))

if num % 2 == 0:
	print('El numero {} es par.'.format(num))

else :
	print('El numero {} es impar'.format(num))