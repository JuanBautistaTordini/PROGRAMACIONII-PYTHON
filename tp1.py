'''
1. Realizar un programa que pida los tres lados de un triángulo e indique el tipo de
triángulo que es según sus lados: Equilátero (tres lados iguales), Isósceles (dos
lados iguales) o Escaleno (tres lados distintos).

lado1 = int(input("Lado 1: "))
lado2 = int(input("Lado 2: "))
lado3 = int(input("Lado 3: "))

if lado1 == lado2:
    if lado2 == lado3:
        print("Es Equilatero")
    else:
        print("Es isosceles")
elif lado1 == lado3:
        print("Es Isosceles")
else: 
     print("Es escaleno")

'''
'''
2. Implemente un programa que a partir del ancho, alto y largo de una habitación
rectangular calcule cuántos litros de pintura se necesitan para pintarla. Suponiendo
que 1 litro de pintura sirve para 10m cuadrados y que la habitación tiene sólo una
puerta de 0,80 de ancho por 2 mts de alto.

ancho = int(input("Ancho: "))
alto = int(input("alto: "))
largo = int(input("largo: "))

area_pared1 = (ancho * alto) 
area_pared1_2= area_pared1 * 2 

area_pared2 = largo * alto
area_pared2_2= area_pared2 * 2

area_puerta = (0.80 * 2)

area_total = area_pared1_2 + area_pared2_2

area_total = area_total - area_puerta

pintura = area_total/ 10

print("litro de pintura necesaria", pintura)
'''

'''
3. Extienda el programa anterior para permitir múltiple cantidad de “manos” de pintura.
ancho = int(input("Ancho: "))
alto = int(input("alto: "))
largo = int(input("largo: "))

area_pared1 = (ancho * alto) 
area_pared1_2= area_pared1 * 2 

area_pared2 = largo * alto
area_pared2_2= area_pared2 * 2

area_puerta = (0.80 * 2)

area_total = area_pared1_2 + area_pared2_2

area_total = area_total - area_puerta

pintura = area_total/ 10

print("litro de pintura necesaria", pintura)

manos = int(input("Cuantas manos quiere dar:"))
litrosmanos = manos * pintura
print(litrosmanos)
'''

# PROBLMA TEORICO

# numero = int(input("hasta donde quiere llegar: "))

# lista=[]

# for i in range(1, numero):
#     if i%3==0 and i%2==0:
#         lista.append(i)

# print(lista)

# 4. Pedir 3 números enteros e implementar un algoritmo para determinar cuál es el
# mayor de los 3 y mostrar un mensaje por pantalla.

# num1 = int(input("Numero 1: "))
# num2 = int(input("Numero 2: "))
# num3 = int(input("Numero 3: "))

# if num1 >= num2 and num1 >= num3:
#     mayor = num1
# elif num2 >= num1 and num2 >= num3:
#     mayor = num2
# else: 
#     mayor = num3

# print(f"El mayor es {mayor}")
            
# 5. Dada una cadena de texto ingresada por consola, decir cuántos “espacios” contiene.

# cadena = input("Ingresa una cadena de texto: ")

# cantidad_espacios = cadena.count(" ")

# print(f"La cadena ingresada contiene {cantidad_espacios} espacios.")

# 6. Realizar un programa que solicite al usuario un número entero positivo, y luego en
# pantalla muestre la secuencia de números desde el 1 hasta el número ingresado.
# Ej: usuario ingresa 10, en pantalla se mostrará 1 2 3 4 5 6 7 8 9 10

# numero = int(input("ingrese numero: "))

# if numero > 0:
#     for i in range(1, numero + 1):
#         print(i, end=" ")

# 7. Realizar un programa que solicite al usuario un número entero positivo, y luego en
# pantalla muestre solamente los números pares desde el 1 hasta el número
# ingresado.
# Ej: usuario ingresa 10, en pantalla se mostrará 2 4 6 8 10

# numero = int(input("Ingrese un numero: "))

# if numero > 0:
#     for i in range(1, numero + 1):
#         if i % 2 == 0:
#             print(i, end=" ")
# else:
#     print("Ingrese un numero positivo")

# 8. Desarrollar un programa que permita al usuario indicar cuantos valores quiere
# ingresar, luego que permita la carga de los valores por teclado y nos muestre
# posteriormente la suma de los valores ingresados y su promedio

# quiere_ingresar = int(input("Ingrese hasta donde quiere llegar: "))

# valores = []

# for i in range(quiere_ingresar):
#     valor= int(input(f"Valor {i + 1}: "))
#     valores.append(valor)


# suma = sum(valores)

# print(f"suma de los valores ingresados es: {suma}")

# ingresa = int(input("hasta de quiere llegar?: "))

# valores = []

# contador = 0

# for i in range (ingresa):
#     valor = int(input(f"valor {i+1}: "))
#     valores.append(valor)
#     contador+=1

# suma = sum(valores)

# promedio = suma/contador

# print(f"la suma es {suma}")

# print(f"el promedio es {promedio}")

# 9. Se desea realizar una aplicación que solicite al usuario tres números enteros
# positivos (A, B, y X), y que muestre por pantalla todos los múltiplos de X que estén
# entre A y B inclusive.

# A = int(input("A: "))
# B = int(input("B: "))
# X = int(input("X: "))

# for i in range(A, B + 1):
#     if i % X == 0:
#         print(i, end=" ")

# A = int(input("A: "))
# B = int(input("B: "))
# X = int(input("X: "))

# for i in range(A, B + 1):
#     if i % X == 0:
#         print(i,end=" ")

# 10. Escriba un programa que permita al usuario ingresar las medidas de 2 lados de un
# rectángulo, y que luego mediante la impresión repetida de un caracter (ej: *) lo dibuje
# en la pantalla. Para este ejercicio tomaremos un máximo de 40 para el lado más
# largo, con el fin de evitar problemas de visualización en la consola. Verificar en los
# datos de entrada que se cumpla este requisito

# lado1 = int(input("Ingrese medida lado 1: "))
# lado2 = int(input("Ingrese medida lado 2: "))

# if 1 <= lado1 <= 40 and 1 <= lado2 <= 40:
#     for i in range(lado2):
#         print('*' * lado1)
# else: 
#     print("incorrecto")

# 11. Escriba un programa que permita el ingreso de números enteros positivos para
# calcular su promedio, el ingreso finaliza cuando el usuario ingresa un número
# negativo. Luego mostrar el promedio y la cantidad de valores que se ingresaron. Ej:
# “El promedio es ….. con un total de …. ingresos.”

# suma = 0

# cantidad = 0

# while True:
#     numero = int(input("Ingrese un numero: "))
    
#     if numero < 0:
#         break
#     suma += numero
#     cantidad += 1
# if numero < 0:
#     promedio = suma / cantidad
#     print(f"El promedio de los numeros igresados es {promedio}")
# else: 
#     print("fin")

# 12. Escriba un programa que permita el ingreso de números enteros positivos,
# finalizando el ingreso con 0, y luego indique si la secuencia estaba ordenada de
# menor a mayor.

# numeros = []

# while True:
#     numero = int(input ("ingrese un numero: "))

#     if numero == 0:
#         break
#     if numero > 0:
#         numeros.append(numero)
#     else:
#         print("fin")

# ordenado = True
# for i in range(len(numeros) - 1):
#     if numeros[i] > numeros[i + 1]:
#         ordenado = False
#         break

# if ordenado:
#     print("Ordenado de menor a mayor")
# else:
#     print("desordenado")

# 13. Se desea realizar una aplicación que solicite al usuario un caracter y un número
# natural N, y que la aplicación muestre en pantalla dicho carácter repetido N veces
# consecutivas.
# Ej: Ingrese un caracter: +
# Ingrese la cantidad de repeticiones: 15
# +++++++++++++++

# caracter = input("Caracter: ")

# N = int(input("Cantidad de caracteres: "))

# print(caracter * N)

# 14. Escriba un programa que dado un texto ingresado por el usuario cuente la cantidad
# total de vocales que aparecen y lo muestre por pantalla

# palabra = input("Palabra: ")
# vocales = "aeiouAEIOU"

# # Contador para la cantidad de vocales
# cantidad_vocales = 0

# # Lista para almacenar las vocales encontradas
# vocalesSS = []

# # Recorre la palabra por índices
# for i in range(len(palabra)):
#     if palabra[i] in vocales:
#         cantidad_vocales += 1
#         vocalesSS.append(palabra[i])

# # Muestra la cantidad total de vocales encontradas
# print(f"Cantidad total de vocales: {cantidad_vocales}")

# # Muestra las vocales encontradas
# print(f"Vocales encontradas: {vocalesSS}")

# 15. Escriba un programa que, dada una oración ingresada muestre por pantalla:
# a. El número total de caracteres en la oración
# b. La cantidad total de letras (consonantes y vocales, sin signos de puntuación)
# c. La cantidad de palabras separadas por uno o más espacios
# En este ejercicio, para simplificar, asumiremos que los posibles caracteres de
# entrada son letras, espacios, dígitos, signos de puntuación, signos de
# interrogación y de exclamación.
# Investigar si hay funciones de strings que nos faciliten la resolución [len(),
# .isalpha(), .split() , etc.]






