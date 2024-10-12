# 1. Implemente una función que, dada una lista de números, devuelva una nueva lista
# que contenga el cuadrado de cada número utilizando list comprehensions.

# nums = []

# def ingresar_lista(nums):
#     num = int(input("Ingrese un número (ingrese 0 para terminar): "))
#     while num > 0:
#         nums.append(num)
#         num = int(input("Ingrese otro número (ingrese 1 o un número menor para terminar): "))
# def cuadrados(nums):
#     return [num ** 2 for num in nums]

# ingresar_lista(nums)

# print(cuadrados(nums))

# 2. Implemente una función que, dada una lista de nombres, devuelva una nueva lista
# que contenga solo los nombres que tengan una longitud mayor o igual a una
# cantidad de caracteres pasada por parámetro, utilizando list comprehensions.

# nombres = []

# def ingresar_nombres(nombres):
#     nombre = input("Ingrese un nombre (ingrese 0 para terminar): ")
#     while nombre!= "0":
#         nombres.append(nombre)
#         nombre = input("Ingrese otro nombre (ingrese 0 para terminar): ")

# def filtrar_nombres(nombres, longitud):
#     return [nombre for nombre in nombres if len(nombre) >= longitud]

# ingresar_nombres(nombres)

# print(filtrar_nombres(nombres))

# 3. Lee el contenido de un archivo de texto llamado "datos.txt" y crea una lista con todas
# las líneas del archivo, utilizando list comprehensions.

# def LeerArchivo():
#     with open("datos.txt", "r") as file:
#         return [linea.strip() for linea in file]

# datos = LeerArchivo()
# print(datos)

# 4. Dado un diccionario de palabras y sus definiciones, crea una lista que contenga sólo
# las palabras que comienzan con una letra específica (por ejemplo, "a") indicada por
# el usuario, utilizando list comprehensions.

# palabras = []

# def llenar_lista(palabras):
#     palabra = input("Ingresar palabra: ")
#     while palabra != '/':
#         palabras.append(palabra)
#         palabra = input("Ingrese una palabra o '/' para terminar: ")
# def filtrar(palabras):
#     letra = input("Ingrese una letra: ")
#     return [palabra for palabra in palabras if palabra[0] == letra]

# llenar_lista(palabras)

# print(filtrar(palabras))

# 5. Dado un rango de números, crea una lista que contenga todos los números primos
# dentro de ese rango utilizando list comprehensions.

# def es_primo(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1): # desde 2 hasta la potencia del numero
#         if n % i == 0:
#             return False
#     return True

# inicio = 10
# fin = 50

# primos = [num for num in range(inicio, fin + 1) if es_primo(num)]

# print(primos)

# 6. Dado un diccionario de personas y sus edades, crea una lista que contenga solo los
# nombres de las personas cuya edad es mayor a una edad ingresada por el usuario,
# utilizando list comprehensions.

# personas = [
#     {'nombre': "Julia", 'edad': 18},
#     {'nombre': "Carlos", 'edad': 25},
#     {'nombre': "Ana", 'edad': 22},
#     {'nombre': "Luis", 'edad': 17}
# ]

# def filtrar_personas(personas, edad):
#     return [persona['nombre'] for persona in personas if persona['edad'] > edad]

# edad = int(input("Ingrese la edad: "))

# print(filtrar_personas(personas, edad))


# 7. Implemente un programa que le pida una palabra al usuario y cuenta la cantidad de
# vocales en ella. El programa deberá pedirle palabras al usuario hasta que éste
# introduzca la palabra “salir”.


# def pedir_palabras():
#     palabras = []
#     while True:
#         palabra = input("Ingrese una palabra (o 'salir' para terminar): ")
#         if palabra.lower() == "salir":
#             break
#         palabras.append(palabra)
#     return palabras

# def contar_vocales(palabras):
#     vocales = "aeiou"
#     cantidad_total = 0
#     for palabra in palabras:
#         cantidad = sum(1 for letra in palabra.lower() if letra in vocales)
#         cantidad_total += cantidad
#     return cantidad_total

# # Solicitar palabras al usuario
# palabras = pedir_palabras()

# # Contar vocales en las palabras ingresadas
# cantidad_vocales = contar_vocales(palabras)

# # Mostrar el resultado
# print(f"La cantidad de vocales en las palabras ingresadas es: {cantidad_vocales}")

# 8. Dada una lista con elementos duplicados, crea una nueva lista que contenga solo los
# elementos únicos utilizando list comprehensions

# lista_original = [1, 2, 2, 3, 4, 4, 5, 5, 6]

# lista_unicos = list(set(lista_original)) #set permite eliminar duplicados en la lista

# print(lista_unicos)

# 9. Dada una lista de números, crea dos listas separadas: una que contenga los
# números pares y otra que contenga los números impares utilizando list
# comprehensions.

# lista1 = []

# def agregar_lista(lista1):
#     num = int(input("Numeros: "))
#     while num!= 0:
#         lista1.append(num)
#         num = int(input("Numeros, 0 para salir: "))

# agregar_lista(lista1)

# pares = [num for num in lista1 if num % 2 == 0]

# impares = [num for num in lista1 if num % 2 != 0]

# print(f"Pares: {pares}")

# print(f"impares: {impares}")

# 10. Dada una lista de diccionarios que contienen información de estudiantes de una
# materia (nombre_apellido, legajo, nota_parcial1, nota_parcial2, nota_final) ,
# utilizando list comprehensions:

# a. Crea una lista que contenga los nombres de todos los estudiantes. Salida
# ejemplo: nombres: ['Pepe', 'María', 'Pedro', 'Ana']

# b. Crea una lista que contenga los nombres de todos los estudiantes que han
# obtenido una calificación superior a 70 en todos los exámenes

# c. Crea una lista que contenga los nombres de todos los estudiantes que han
# obtenido una calificación inferior a 60 en al menos un examen.

estudiantes = [
    {"nombre_apellido": "Pepe González", "legajo": "123", "nota_parcial1": 80, "nota_parcial2": 75, "nota_final": 85},
    {"nombre_apellido": "María López", "legajo": "124", "nota_parcial1": 90, "nota_parcial2": 95, "nota_final": 92},
    {"nombre_apellido": "Pedro Martínez", "legajo": "125", "nota_parcial1": 50, "nota_parcial2": 55, "nota_final": 60},
    {"nombre_apellido": "Ana Fernández", "legajo": "126", "nota_parcial1": 70, "nota_parcial2": 65, "nota_final": 75},
]

nombres = [estudiante["nombre_apellido"].split()[0] for estudiante in estudiantes]
print(f"Nombres: {nombres}")


nombres_superiores_70 = [
    estudiante["nombre_apellido"].split()[0] for estudiante in estudiantes
    if (estudiante["nota_parcial1"] > 70 and
        estudiante["nota_parcial2"] > 70 and
        estudiante["nota_final"] > 70)
]
print(f"Estudiantes con todas las notas superiores a 70: {nombres_superiores_70}")

nombres_inferiores_60 = [
    estudiante["nombre_apellido"].split()[0] for estudiante in estudiantes
    if (estudiante["nota_parcial1"] < 60 or
        estudiante["nota_parcial2"] < 60 or
        estudiante["nota_final"] < 60)
]
print(f"Estudiantes con al menos una nota inferior a 60: {nombres_inferiores_60}")
