# 1. Inicializar una lista vacía para almacenar los números
lista_numeros = []

# Explicación del control de errores:
# Usamos un bucle para pedir exactamente 3 números.
# Si el usuario se equivoca, el bloque try-except atrapa el error y le vuelve a preguntar.
for i in range(3):
    while True:
        try:
            # Pedir el número al usuario y convertirlo a decimal (float)
            entrada = input(f"Ingresa el número {i + 1} de 3: ")
            numero = float(entrada)
            
            # Si la conversión es exitosa, se agrega a la lista y se rompe el bucle interno
            lista_numeros.append(numero)
            break
        except ValueError:
            # Este bloque se ejecuta si el usuario ingresa letras o símbolos no válidos
            print("Error: Entrada no válida. Por favor, introduce un número real o entero.")

# 2. Calcular el promedio sumando los elementos y dividiendo por la cantidad
# Se usa len() para asegurar dinamismo, aunque sabemos que son 3 elementos
promedio = sum(lista_numeros) / len(lista_numeros)

# 3. Mostrar el resultado por pantalla
print(f"\nLos números ingresados fueron: {lista_numeros}")
print(f"El promedio calculado es: {promedio:.2f}")
