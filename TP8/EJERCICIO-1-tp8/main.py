# main.py
from Libro import Libro

import json


class Tester:
    @staticmethod
    def cargar_libros():
        # Abre el archivo 'data/libros.json' en modo lectura
        with open('C:/Users/bauti/OneDrive/Escritorio/TUP/Programacion II/tps/TP8/EJERCICIO-1-tp8/libros.json', 'r', encoding='utf-8') as file:
            # Carga los datos del archivo JSON en una lista de diccionarios
            data = json.load(file)
            # Crea una lista de objetos Libro a partir de los diccionarios
            libros = [Libro.fromDiccionario(dic) for dic in data]
            return libros

    @staticmethod
    def mostrar_libros(libros):
        # Indentación corregida: Itera sobre la lista de libros y muestra la información de cada uno
        for libro in libros:
            print(f"Título: {libro.get_titulo()}, Autor: {libro.get_autor()}, Género: {libro.get_genero()}, Año de Publicación: {libro.get_ano_publicacion()}, ISBN: {libro.get_isbn()}")

    @staticmethod
    def buscar_por_ano(libros, ano):
        # Crea una lista de libros cuyo año de publicación coincide con el año ingresado
        resultados = [libro for libro in libros if libro.ano_publicacion == ano]
        return resultados

if __name__ == "__main__":
    # Carga los libros desde el archivo 'data/libros.json'
    libros = Tester.cargar_libros()
    # Muestra todos los libros cargados
    Tester.mostrar_libros(libros)
    
    # Solicita al usuario ingresar un año de publicación para buscar libros
    ano = int(input("Ingrese el año de publicación para buscar libros: "))
    resultados = Tester.buscar_por_ano(libros, ano)
    
    if resultados:
        print("Libros encontrados:")
        Tester.mostrar_libros(resultados)
    else:
        print("No se encontraron libros para el año ingresado.")
