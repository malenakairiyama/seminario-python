# Haz un programa que pida al usuario que ingrese una temperatura en 
# grados Celsius y luego convierta esa temperatura a grados Fahrenheit,
# mostrando el resultado.
temp_celsius = input("Ingrese una temperatura en celsius: ")
temp_fahr = (int(temp_celsius)*9/5)+32
print(f"La temperatura ingresada es igual a {temp_fahr} grados Fahrenheit") 
