# Convertir un String a una operacion e imprimir el resultado

operacion = input('Escribe una Operacion: ').replace(" ", "")

# Variables
bSuma = operacion.find('+')
bResta = operacion.find('-')
bMulti = operacion.find('*')
bDiv = operacion.find('/')
num1 = 0
num2 = 0
resultado = 0.0

if bMulti >= 1:
    num1 = float(operacion[0:bMulti])
    num2 = float(operacion[(bMulti+1):len(operacion)])
    resultado = num1 * num2
    print('El resultado de la multiplicacion es: ', resultado)
elif bDiv >= 1:
    num1 = float(operacion[0:bDiv])
    num2 = float(operacion[(bDiv+1):len(operacion)])
    resultado = num1 / num2
    print('El resultado de la division es: ', resultado)
elif bSuma >= 1:
    num1 = float(operacion[0:bSuma])
    num2 = float(operacion[(bSuma+1):len(operacion)])
    resultado = num1 + num2
    print('El resultado de la suma es: ', resultado)
elif bResta >= 1:
    num1 = float(operacion[0:bResta])
    num2 = float(operacion[(bResta+1):len(operacion)])
    resultado = num1 - num2
    print('El resultado de la resta es: ', resultado)
else:
    print('Operacion no valida')
