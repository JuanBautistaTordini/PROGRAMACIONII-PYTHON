import json

from clases.libro import libro


class Tester:
    @staticmethod
    def cargar_libros():
        # Abre el archivo 'libros.json' en modo lectura
        with open('libros.json', 'r', encoding='utf-8') as file:
            # Carga los datos del archivo JSON en una lista de diccionarios
            data = json.load(file)
            # Crea una lista de objetos Libro a partir de los diccionarios
            libros = [Libro.fromDiccionario(dic) for dic in data]
            return libros

    @staticmethod
    def mostrar_libros(libros):
        # Itera sobre la lista de libros y muestra la información de cada uno
        for libro in libros:
            print(f"Título: {libro.titulo}, Autor: {libro.autor}, Género: {libro.genero}, Año de Publicación: {libro.ano_publicacion}, ISBN: {libro.isbn}")

    @staticmethod
    def buscar_por_ano(libros, ano):
        # Crea una lista de libros cuyo año de publicación coincide con el año ingresado
        resultados = [libro for libro in libros if libro.ano_publicacion == ano]
        return resultados

if __name__ == "__main__":
    # Carga los libros desde el archivo 'libros.json'
    libros = Tester.cargar_libros()
    # Muestra todos los libros cargados
    Tester.mostrar_libros(libros)
    
    # Solicita al usuario ingresar un año de publicación para buscar libros
    ano = int(input("Ingrese el año de publicación para buscar libros: "))
    # Busca libros cuyo año de publicación coincide con el año ingresado
    resultados = Tester.buscar_por_ano(libros, ano)
    
    if resultados:
        # Si se encontraron libros, los muestra
        print("Libros encontrados:")
        Tester.mostrar_libros(resultados)
    else:
        # Si no se encontraron libros, muestra un mensaje de error
        print("No se encontraron libros para el año ingresado.")