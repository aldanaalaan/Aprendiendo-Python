# continue y break
print('Imprimir lo numeros impares en un intervalo de numeros,\n hasta llegar a un multiplo de 15')
inicio = int(input('Dame el numero donde empieza el intervalo: '))
fin = int(input('Dame el numero donde termina: ')) + 1

for i in range(inicio, fin):
    
    if i % 2 == 0:
        continue
        
    if i % 15 == 0:
        print(i)
        break

    print(i, end = ', ')