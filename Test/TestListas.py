# Buscar una subcadena dentro de las cadenas de una lista

# Lista de muestra para probar el algoritmo
listaColores = ['Azul', 'Rojo', 'Morado',
                'Gris', 'Celeste', 'Blanco y Negro', 'negro']

# Variables
a = input('Dime que cadena voy a buscar: ')
a = a.lower()
listaPLista = []
listaPCadena = []
encontrado = False

# Ciclo encargado de buscar la subcadena
for i in listaColores:
    cadColor = i.lower()
    if cadColor.find(a) >= 0:
        encontrado = True
        listaPLista.append(i)
        listaPCadena.append(cadColor.find(a))

# Reinicio del indice
i = 0

# Ciclo encargado de imprimir los resultados
while encontrado and i < len(listaPCadena):
    print('La cadena buscada se encuentra en la posicion de lista {} y en la posicion de cadena {}'.format(
        listaPLista[i], listaPCadena[i]))
    i += 1

if not encontrado:
    print('La cadena no fue encontrada')
