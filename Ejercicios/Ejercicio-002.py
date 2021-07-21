# Manipulacion de cadenas

# Asignacion
print('ASIGNACION:')
mensaje = 'Hola'
mensaje += ' '
mensaje += 'Alan'

print(mensaje)

# Concatenacion
print('CONCATENACION:')
mensaje = 'Hola'
espacio = ' '
nombre = 'Alan'

print(mensaje + espacio + nombre)

# CONCATENACION CON NUMEROS
num1 = 4
num2 = 6
resultado = num1 + num2

# Convertir int a Str
resultado = str(resultado)

print('El resultado de la suma es: ' + resultado)

# Multiplicacion
mensaje = 'Hey! '

print(mensaje * 3)

# BUSQUEDA
print('BUSQUEDA:')
mensaje = 'Hola Alan'
buscar_Subcadena = mensaje.find('Alan')

print(buscar_Subcadena)

# EXTRACCION
print('EXTRACCION:')
mensaje = 'Hola Alan'
extraer_Subcadena = mensaje[1:8]

print(extraer_Subcadena)

# COMPARACION
print('COMPARACION:')
mensaje1 = 'Hola'
mensaje2 = 'Hola'

print(mensaje1 == mensaje2)

# MEDIR STRING
print('MEDIR STRING:')
mensaje = 'Hello World'
longitud = len(mensaje)

print('La cadena {} tiene una longitud de {}'.format(mensaje, longitud))
