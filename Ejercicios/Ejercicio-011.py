# Listas
numeros = [1, 2, 3, 5, 6, 7, 8,9, 10]

i = 0

while i <= 10:
    longitud = len(numeros)
    longitud += 1
    numeros.insert(longitud, int(input('Dame el siguiente numero: ')))
    i += 1

print(numeros)

numeros.remove(10)

print(numeros)