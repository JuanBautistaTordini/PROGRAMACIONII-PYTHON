from contacto import Contacto
import json

class Tester: 
    def almacenar_contactos(self, contactos):
        with open("TP8\EJERCICIO-2-tp8\contactos.json", "w") as file:
            json.dump([contacto.toDiccionario() for contacto in contactos], file) 
        print("Contactos guardados en 'contactos.json'.")  # Confirmación de guardado
        return contactos
    
    def cargar_contactos(self):
        try:
            with open("contactos.json", "r", encoding='UTF-8') as file:
                data = json.load(file)
                contactos = [Contacto.fromDiccionario(dicc) for dicc in data]
            print("Contactos cargados desde 'contactos.json'.")  # Confirmación de carga
            return contactos
        except FileNotFoundError:
            print("Error: El archivo 'contactos.json' no existe.", errcode())
            return []

    def buscar_contactos_por_apellido(self, letra):
        contactos = self.cargar_contactos()
        resultados = [contacto for contacto in contactos if contacto.apellido.startswith(letra)]
        return resultados

def main():
    tester = Tester()
    contactos = [
        Contacto("Juan", "Perez", "123456789", "juanperez@gmail.com", "Calle Falsa 123"),
        Contacto("Juan", "Heguy", "123456789", "juanheguy@gmail.com", "Calle Verdadera 123"),
        Contacto("Juan", "Tordini", "123456789", "juantordini@gmail.com", "Calle Real 123")
    ]
    
    # Almacenar los contactos en el archivo JSON
    tester.almacenar_contactos(contactos)
    
    # Solicita al usuario ingresar la primera letra del apellido
    letra = input("Ingrese una letra: ").strip()
    resultados = tester.buscar_contactos_por_apellido(letra)
    
    if resultados:
        print("Apellidos encontrados:")
        for contacto in resultados:
            print(contacto)
    else:
        print("No se encontraron apellidos para la letra ingresada.")

if __name__ == "__main__":
    main()
