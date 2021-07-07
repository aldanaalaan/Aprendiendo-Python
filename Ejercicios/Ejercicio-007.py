# Sentencias condicionales

# IF
# Felicitar a un alumno si su promedio es aprobatoria
print('IF:')

nombre = input('Hola, ¿Como te llamas? ')
cal1 = float(input('{}, ¿Cual es tu calificacion en matematicas? '.format(nombre)))
cal2 = float(input('{}, ¿Cual es tu calificacion en quimica? '.format(nombre)))
cal3 = float(input('{}, ¿Cual es tu calificacion en biologia? '.format(nombre)))
promedio = (cal1 + cal2 + cal3)/3

if promedio >= 6:
    print('Felicidades {}, aprobaste.'.format(nombre))

print('Tu promedio es de {}'.format(promedio))

print('FIN')
print('')
# IF-ELSE
# Saber si un numero es negativo o positivo
print('IF-ELSE:')

num = int(input('Dame un numero: '))

if num >= 0:
    print('El numero {} es positivo.'.format(num))
else:
    print('El numero {} es negativo.'.format(num))

print('FIN')
print('')
# ELIF
print('ELIF:')

# Imprimir un tipo de dato

num1 = 24
cad1 = 'Hola Mundo'
dec1 = 453.8
print('¿Que tipo de dato quieres obtener?')
print('[1] Entero')
print('[2] String')
print('[3] Flotante')
print('')

opcion=int(input())

if opcion == 1:
    print(str(num1))
elif opcion == 2:
    print(cad1)
elif opcion == 3:
    print(str(dec1))
else :
    print('La opcion {} no esta disponible'.format(opcion))
print('FIN')