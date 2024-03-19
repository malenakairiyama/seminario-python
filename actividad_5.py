#Implementa un programa que solicite al usuario que ingrese una lista
#de números. Luego, imprime la lista pero detén la impresión si 
# encuentras un número negativo. Nota: utilice la sentencia break 
# cuando haga falta.

# Solicitar al usuario que ingrese los números separados por comas
entrada = input("Ingresa los números separados por comas: ")

# Dividir la entrada en una lista de números
numeros_texto = entrada.split(',')

# Convertir cada número de texto a un número entero
numeros = [int(numero) for numero in numeros_texto]

# Imprimir la lista de números ingresados
#print("Lista de números ingresados:", numeros)

#Imprimir lista deteniendo la operacion si el número es negativo
for numero in numeros:
    if numero < 0:
        print("Número negativo - fin de la impresión")
        break 
    print(numero)
