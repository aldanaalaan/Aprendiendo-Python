# Entrada de datos en Python

# Variables
nombre = ''
num1 = 0
num2 = 0
resultado = 0

# Pedir nombre
nombre = input('Dime tu nombre: ')
print('Hola {}, vamos a hacer una suma'.format(nombre))

# Pedir numeros
num1 = int(input('Dame el primer numero entero: '))
num2 = int(input('Dame el segundo numero entero: '))
resultado = int(num1 + num2)

# Mostrar resultado
print('{}, el resultado de la suma de {} y {} es: {}'.format(
    nombre, num1, num2, resultado))
