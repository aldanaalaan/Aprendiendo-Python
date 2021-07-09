# Programa para resolver ecuaciones cuadraticas

# Ingreso de datos
coa = int(input('Dame el coeficiente del termino cuadratico: '))
cob = int(input('Dame el coeficiente del termino lineal: '))
coc = int(input('Dame el termino independiente: '))

# Indicador de numero de soluciones
ind = (cob ** 2) - (4 * (coa * coc))

#Soluciones
x1 = (-cob + (ind ** 0.5))/ (2 * coa)
x2 = (-cob - (ind ** 0.5))/ (2 * coa)

# Agregar signo (+) a los positivos b y c
if cob > -1:
	cob = '+' + str(cob)

if coc > -1:
	coc = '+' + str(coc)

# Impresion de resultados
if ind >= 1:
	print('La ecuacion {}x²{}x{} tiene dos soluciones'.format(coa, cob, coc))
	print('Las soluciones para x en la ecuacion {}x²{}x{} son {} y {}'.format(coa, cob, coc, x1, x2))
elif ind == 0:
	print('La ecuacion {}x²{}x{} tiene un soluciones'.format(coa, cob, coc))
	print('La solucion para x en la ecuacion {}x²{}x{} es {}'.format(coa, cob, coc, x1))
else:
	print('La ecuacion {}x²{}x{} no tiene soluciones'.format(coa, cob, coc))