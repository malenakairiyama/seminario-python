#Escribe un programa que tome una lista de números enteros como entrada 
#del usuario. Luego, convierte cada número en la lista a string y únelos 
#en una sola cadena, separados por guiones ('-'). Sin embargo, excluye 
#cualquier número que sea múltiplo de 3 de la cadena final.

# Solicitar al usuario que ingrese los números separados por espacios
entrada = input("Ingresa los números enteros separados por espacios: ")


# convierte la cadena ingresada en una lista de números en texto
numeros_texto = entrada.split(',')

# Crear una lista vacía para almacenar los números filtrados
numeros_filtrados = []

# Filtrar los números y agregar los números filtrados a la lista
for numero in numeros_texto:
    if (int(numero)) % 3 != 0:
        numeros_filtrados.append(numero)

# Convertir cada número filtrado a una cadena de texto y agregarlos a la lista final
numeros_filtrados_texto = []
for numero in numeros_filtrados:
    numeros_filtrados_texto.append(str(numero))

# Unir las cadenas de texto con guiones
cadena_final = '-'.join(numeros_filtrados_texto)

# Imprimir la cadena final
print("Cadena final: ", cadena_final)
       