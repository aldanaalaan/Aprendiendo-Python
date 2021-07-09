# Inversor de cadenas

print('*********************')
print('*INVERSOR DE CADENAS*')
print('*********************')

# Guardar cadena
cad = input('Dame una cadena de texto para invertir: ')

# Variables
longitud = len(cad)
i = 0
cadInv = ""

# Ciclo para invertir la cadena
while i <= longitud:
	cadInv += cad[longitud:(longitud+1)]
	longitud -= 1

# Imprimir cadena invertida
print('La cadena "{}" invertida es "{}"'.format(cad, cadInv))