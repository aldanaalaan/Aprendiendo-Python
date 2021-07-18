# Programa para resolver ecuaciones cuadraticas

# Ingreso de datos
coa = int(input('Dame el coeficiente del termino cuadratico: '))
cob = int(input('Dame el coeficiente del termino lineal: '))
coc = int(input('Dame el termino independiente: '))

# Indicador de numero de soluciones
ind = (cob ** 2) - (4 * (coa * coc))

# Soluciones
x1 = (-cob + (ind ** 0.5)) / (2 * coa)
x2 = (-cob - (ind ** 0.5)) / (2 * coa)

# Agregar signo (+) a los positivos b y c
if cob > -1:
    cob = '+' + str(cob)

if coc > -1:
    coc = '+' + str(coc)

# Impresion de resultados
if ind >= 1:
    print(f'La ecuacion {coa}x²{cob}x{coc} tiene dos soluciones')
    print(
        f'Las soluciones para x en la ecuacion {coa}x²{cob}x{coc} son {x1} y {x2}')
elif ind == 0:
    print(f'La ecuacion {coa}x²{cob}x{coc} tiene un soluciones')
    print(f'La solucion para x en la ecuacion {coa}x²{cob}x{coc} es {x1}')
else:
    print(f'La ecuacion {coa}x²{cob}x{coc} no tiene soluciones')
