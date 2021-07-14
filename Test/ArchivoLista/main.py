# Lista por archivo
handled = open('lista.txt')
l = []
for i in handled:
    l.append(i.rstrip())
# Metodos de listas
print('Hola usuario')

while True:

    print('Menu de opciones'.upper())
    print('[1] Agregar elemento\n[2] Eliminar elemento\n[3] Mostrar elementos\n[4] Guardar y salir')
    opc = input('¿Que quieres hacer? ')
    opc = int(opc)
    if opc == 1:

        elemento = input('Dime que elemento agregar: ')
        elemento = int(elemento)
        l.append(elemento)

    elif opc == 2:

        if l == []:

            print('La lista ya está vacia.')
            continue

        contador = 1

        for i in l:

            print(str(contador) + '. ' + str(i))
            contador += 1

        numEl = input('Dime que elemento eliminar: ')
        numEl = int(numEl)

        if numEl > len(l) or numEl < 1:

            print('El elemento seleccionado no se encuentra en la lista.')
            continue

        l.remove(l[numEl - 1])
        print(f'Elemento {numEl} eliminado.')

    elif opc == 3:

        if l == []:
            print('La lista está vacia.')
            continue

        contador = 1
        for i in l:

            print(str(contador) + '. ' + str(i))
            contador += 1

    elif opc == 4:

        print('Adios usuario')
        break

    else :

    	print('La opcion no está disponible.')
handled.close()
handled = open('lista.txt', 'w')

for i in l:

    handled.write(str(i) + '\n')

handled.close()