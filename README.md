# TPI-AySO
TRABAJO PRACTICO INTEGRADOR AREUITECTURA Y SISTEMAS OPERATIVOS UTN SAN NICOLAS

# Calculadora de Promedio

Programa simple en Python que solicita al usuario tres números, calcula su promedio y muestra el resultado por pantalla.

## Descripción

El script pedirá al usuario que ingrese exactamente **3 números** (enteros o decimales). Una vez ingresados, calcula el promedio y lo muestra con dos decimales de precisión. Incluye manejo de errores para entradas no válidas.

## Requisitos

- Python 3.x

No requiere librerías externas.

## Uso

Desde la raíz del proyecto, ejecutá:

```bash
python promedio.py
```

### Ejemplo de ejecución

```
Ingresa el número 1 de 3: 10
Ingresa el número 2 de 3: 20
Ingresa el número 3 de 3: 30

Los números ingresados fueron: [10.0, 20.0, 30.0]
El promedio calculado es: 20.00
```

### Manejo de errores

Si se ingresa un valor no válido (letras o símbolos), el programa notifica el error y vuelve a solicitar el mismo número:

```
Ingresa el número 1 de 3: abc
Error: Entrada no válida. Por favor, introduce un número real o entero.
Ingresa el número 1 de 3:
```

## Estructura del proyecto

```
/
└── promedio.py   # Script principal
└── README.md     # Este archivo
```

## Lógica del programa

1. Se inicializa una lista vacía para almacenar los números ingresados.
2. Se solicitan 3 números mediante un bucle `for`, con validación de entrada usando `try-except`.
3. Se calcula el promedio con `sum() / len()`.
4. Se imprime la lista de números y el promedio formateado con 2 decimales.
