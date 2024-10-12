# def reverso(cadena):
#     return cadena[::-1]

# def es_palindromo(cadena):
#     cadena = cadena.lower()
#     return cadena == reverso(cadena)

# cadena = input("Ingree una cadena: ")

# cadena_inverso = reverso(cadena)

# print(f"cadena inversa: {cadena_inverso}")

# if es_palindromo(cadena):
#     print(f"{cadena} es palindromo")
# else:
#     print(f"{cadena} no es palindromo")

# 2. Escriba una función llamada EsBisiesto que permita ingresar un número de año y
# devuelva verdadero en caso que el año sea bisiesto, o falso cuando no lo es. Un año
# es bisiesto si: es divisible entre cuatro y (no es divisible entre 100 o es divisible entre
# 400). Utilizarlo en un programa que permita ingresar dia, mes y año y muestre por
# pantalla si la fecha es válida o no.

# funcion para determinar si es bisiesto
# def EsBisiesto(ano):
#     return (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0)

# def fecha_valida(dia, mes, ano):
#      #Año "normal"
#      dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#      #si es bisiesto se cambia febreo
#      if EsBisiesto(ano):
#          dias_por_mes[1] = 29
    
#      #verificar mes
#      if mes < 1 or mes > 12:
#          return False
    
#      #verificar dias del rango
#      if dia < 1 or dia > dias_por_mes[mes - 1]:
#          return False
    
#      #si no pasa a false 
#      return True

# dia = int(input("dia: "))
# mes = int(input("mes: "))
# ano = int(input("año: "))

# if (fecha_valida(dia, mes, ano)):
#     if EsBisiesto(ano):
#         print("Fecha valida, año bisiesto")
#     else:
#         print("Fecha valida, año no bisiesto")

# else: 
#     print("fecha no valida")

# 3. Escriba un programa que permita cargar las notas de exámenes, primero debe
# permitir ingresar por teclado la cantidad de notas que desea cargar, y luego
# cargarlas en una lista, y posteriormente debe buscar la nota más alta, mostrarla, e
# indicar en qué índice del arreglo se encuentra.

# cantidad = int(input("Cantidad de notas: "))

# NotasDeExamanes = []

# for i in range(cantidad):
#     nota = float(input(f"nota {i + 1}: "))
#     NotasDeExamanes.append(nota)

# NotaMasAlta = max(NotasDeExamanes)

# print(f"la nota mas alta entre {NotasDeExamanes} es {NotaMasAlta}")

# 4. Escriba un programa que permita ingresar un número, se debe validar que
# realmente se haya ingresado un número, y crear una lista para almacenar por
# separado los dígitos del número. Luego recorrer la lista y mostrar el índice que
# contiene el dígito mayor.

# def esValido():
#     numero = input("Ingrese un número: ")
#     if numero.isdigit():
#         return int(numero)
#     else:
#         print("No se ha ingresado un número válido. Inténtelo de nuevo.")
#         return None

# def digitosDelNumero(numero):
#     return [int(digito) for digito in str(numero)]

# def digitoMayor(digitos):
#     digitoMayor = max(digitos)
#     indice = digitos.index(digitoMayor)
#     return digitoMayor, indice

# numero = None

# while numero is None:
#     numero = esValido()

# digitos = digitosDelNumero(numero)

# digitoMayor, indice = digitoMayor(digitos)

# print(f"El digito mayor es {digitoMayor} y se encuentra en la posicion {indice+1}")

# 5. Escriba un programa que permita cargar una lista de alumnos junto con su nota del
# parcial. Seleccione la estructura de datos que mejor se adapte al problema. Luego
# de ingresados los datos debe generar una lista donde figure si aprobaron o no (se
# aprueba con 40 o más). El listado a mostrar por pantalla debe ser como el siguiente
# (el resultado no se almacena, se calcula):
# ALUMNOS PARCIAL RESULTADO
# Smith, Juan 70 Aprobado
# Suárez, María 35 Desaprobado4

# Función para cargar los datos de un alumno
# def cargar_datos(alumno):
#     nombre = input(f"Ingrese el nombre del alumno {alumno + 1}: ")
#     nota = float(input(f"Ingrese la nota del alumno {alumno + 1}: "))
#     return nombre, nota

# # Función para generar el listado
# def generar_listado(alumnos):
#     print("ALUMNOS PARCIAL RESULTADO")
#     for alumno in alumnos:
#         nombre, nota = alumno
#         if nota >= 40:
#             resultado = "Aprobado"
#         else:
#             resultado = "Desaprobado"

#         print(f"{nombre}, {nota} {resultado}")

# # Ingreso de datos de los alumnos
# alumnos = []

# cantidadDeAlumnos = int(input("Ingrese cantidad de alumnos: "))

# for i in range(cantidadDeAlumnos):
#     alumno = cargar_datos(i)
#     alumnos.append(alumno)

# generar_listado(alumnos)

# 6. Escriba un programa que permita leer de un archivo distancias.txt (cada renglón
# tiene una distancia válida) las distancias recorridas por el vehículo de una empresa,
# luego calcular cual es la distancia promedio, y mostrar por pantalla el promedio y
# todas las distancias mayores al promedio.
# Ej del contenido del archivo:
# 150
# 120
# 50
# 34
# 250
# Salida: “La distancia promedio de los viajes es … y los viajes con distancia mayor
# son: … , … , …. , …. “

# with open("distancias.txt", "r") as file:
#     distancias = [float(distancia) for distancia in file.readlines()]
#     promedio = sum(distancias) / len(distancias)

#     distanciaMayorAlPromedio = [distancia for distancia in distancias if distancia > promedio]
    
#     print(f"el promedio es: {promedio}")
#     print(f"distancia mayor al promedio {distanciaMayorAlPromedio}")

# 7. Un almacén guarda los códigos, los nombres de los productos y sus precios,
# respectivamente, separados por punto y coma ( ; ) en el archivo productos.txt. Hacer
# un algoritmo y luego los procedimientos necesarios que permitan tomar los datos del
# archivo y buscar el precio de un artículo ingresado por teclado. Para probar el
# algoritmo crear un archivo “productos.txt” y cargarle datos al estilo:
# 100;arroz;10
# 102;fideos;5
# 135;lentejas;8
# 138;porotos;6
# 140;sal gruesa;5
# 201;aceite;20 ( etc… )

 


# 8. El mismo almacén del punto anterior almacena los datos del stock de productos en
# el archivo stock.txt separados por punto y coma ( ; ) con el formato “codigo de
# producto; stock mínimo; stock real”. Escriba un programa, que a partir de
# información contenida en los archivos, genere otro archivo de texto, Compras.txt,
# conteniendo todos los productos cuyo stock se encuentra por debajo del mínimo.
# Utilizar el archivo productos.txt del punto anterior, y crear un archivo stock.txt y
# cargarle datos utilizando los códigos de los productos del archivo anterior. Ej:
# 100;50;60
# 102;50;20
# 135;20;15
# 138;20;20
# 140;10;8
# 201;20;30 ( etc… )

# productos = {}

# stock={}

# with open("productos.txt", "r") as file:
#     for linea in file:
#         codigo, nombre, precio = linea.strip().split(";")
#         productos[nombre.lower()] = float(precio)

# with open("stock.txt", "r") as file:
#     for linea in file:
#         codigo, stockMinimo, stockReal = linea.strip().split(";")
#         stock[codigo] = (int(stockMinimo), int(stockReal))  

# with open("compras.txt", "w") as file:
#     for codigo, (stockMinimo, stockReal) in stock.items():
#         if stockReal < stockMinimo:
#             file.write(f"codigo: {codigo};Stock Min: {stockMinimo};Stock Real: {stockReal}\n")

# print ("Archivo txt creado con exito")

# productoABuscar = input("Producto: ")

# if productoABuscar in productos:
#     print(f"El precio del producto {productoABuscar} es: ${productos[productoABuscar]}")
# else:
#     print("Producto no encontrado")

# 9. Un profesor almacenó los datos de los alumnos de su materia en un archivo
# alumnos.txt. En cada línea guardó el número de legajo del alumno y sus tres notas
# finales (oral, escrito y trabajos prácticos). El archivo está ordenado por número de
# legajo.
# En otro archivo, ordenado alfabéticamente por apellido, guarda por línea, número de
# legajo, apellido y nombre de cada uno.
# En ambos archivos los datos están separados por punto y coma ( ; ) .
# Desea escribir un programa para generar un archivo Promoción.txt con los apellidos
# y nombres de los alumnos que promocionan la materia, esto es, alumnos que el
# promedio de las tres notas supere los 7 puntos.
# El archivo debe quedar ordenado alfabéticamente

# # Leer el archivo y calcula los promedios
# alumno_notas ={}
# with open("alumnos.txt", "r") as file:
#     for line in file:
#         legajo, oral, escrito, trabajos = line.strip().split(";")
#         oral = float(oral)
#         escrito = float(escrito)
#         trabajos = float(trabajos)
#         promedio = (oral + escrito + trabajos) / 3
#         alumno_notas[legajo] = promedio

# alumnos_promocion=[]

# with open("alumnos_ordenados.txt", "r") as file:
#     for line in file:
#         legajo, apellido, nombre = line.strip().split(";")
#         if legajo in alumno_notas and alumno_notas[legajo]>7:
#             alumnos_promocion.append((apellido, nombre))

# alumnos_promocion.sort()  # Ordenamos alfabéticamente los alumnos

# with open("promocion.txt", "w") as file:
#     for apellido, nombre in alumnos_promocion:
#         file.write(f"{apellido}, {nombre}\n")

# print("Archivo Promoción.txt creado con exito")


        
