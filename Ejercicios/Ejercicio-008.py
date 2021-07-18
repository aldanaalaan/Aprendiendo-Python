'''
La compañia Rappi pide un Sistema que determine los dias de vacaciones de un trabajador.
Existen tres departamentos:

- Dep. Atencion al cliente (Clave 1)
	- Con un año reciben 6 dias
	- Con 2-6 años de servicio reciben 14 dias
	- Con 7 o más años reciben 20 dias
- Dep. de Logistica (Clave 2)
	- 1 - 7 dias
	- 2-6 - 15 dias
	- +7 - 22 dias
- Gerencia (Clave 3)
	- 1 - 10
	- 2-6 - 20
	- +7 - 30

Debe solicitar nombre, clave y antiguedad.
'''

# Titulo
print('*******************************************')
print('*Bienvenido al sistema vacacional de Rappi*')
print('*******************************************')

# Pedir datos
nombre = input('Hola empleado, ¿Como te llamas? ')
clave = int(input(nombre + ', ¿Cual es la clave de tu departamento? '))
an = int(input(nombre + ', ¿Cuantos años llevas en la compañia? '))

# Condicional departamento
if clave == 1:

    if an == 1:
        print(nombre + ', tienes derecho a 6 dias de vacaciones')
    elif an >= 2 and an <= 6:
        print(nombre + ', tienes derecho a 14 dias de vacaciones')
    elif an >= 7:
        print(nombre + ', tienes derecho a 20 dias de vacaciones')
    else:
        print(nombre + ', todavia no tienes derecho a vacaciones')

elif clave == 2:

    if an == 1:
        print(nombre + ', tienes derecho a 7 dias de vacaciones')
    elif an >= 2 and an <= 6:
        print(nombre + ', tienes derecho a 15 dias de vacaciones')
    elif an >= 7:
        print(nombre + ', tienes derecho a 22 dias de vacaciones')
    else:
        print(nombre + ', todavia no tienes derecho a vacaciones')

elif clave == 3:

    if an == 1:
        print(nombre + ', tienes derecho a 10 dias de vacaciones')
    elif an >= 2 and an <= 6:
        print(nombre + ', tienes derecho a 20 dias de vacaciones')
    elif an >= 7:
        print(nombre + ', tienes derecho a 30 dias de vacaciones')
    else:
        print(nombre + ', todavia no tienes derecho a vacaciones')

else:
    print('La clave del departamento no es valida')
