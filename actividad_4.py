#Cree un programa que dada una lista de números imprima sólo los 
# que son pares. Nota: utilice la sentencia continue donde haga falta.

numeros = [1, 2, 3, 4, 5, 6]

for num in numeros:
    if num % 2 == 0:
        print(f"{num} es par")
    else:
        continue