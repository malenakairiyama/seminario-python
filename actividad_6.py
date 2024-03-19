#Modifique el ejercicio 4 para que dada la lista de número genere 
#dos nuevas listas, una con los número pares y otras con los que son 
#impares. Imprima las listas al terminar de procesarlas.

numeros = [14, 67, 35, 88, 126, 95, 73, 62, 148]

lista_pares = []
lista_impares = []

for num in numeros:
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)

print(f"Lista numeros pares: {lista_pares}")
print(f"Lista impares: {lista_impares}")
