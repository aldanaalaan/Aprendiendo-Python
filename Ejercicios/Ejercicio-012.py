# Calcular el numero de vocales de una frase con for

cad1 = input('Dame una cadena: ')
cad2 = cad1.lower()
contador = 0
for i in cad2:
	if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
		contador += 1

print('La cadena "{}" tiene {} vocales'.format(cad1, contador))