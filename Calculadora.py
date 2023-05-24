#CALCULADORA
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

#Solitando números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

#Realizar las operaciones
resultado_suma = suma(num1,num2)
resultado_resta = resta(num1,num2)
resultado_multiplicacion = multiplicacion(num1,num2)
resultado_division = division(num1,num2)

#Imprimir resultados
print("Suma: ", resultado_suma)
print("Resta: ", resultado_resta)
print("Multiplicacion: ", resultado_multiplicacion)
print("Division: ", resultado_division)

