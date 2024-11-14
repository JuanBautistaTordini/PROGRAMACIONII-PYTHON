from contacto import Contacto
import json

'''
clase tester:
a. Crea objetos de la clase Contacto y almacenarlos en una lista
b. Guarda esa lista completa en un archivo JSON “contactos.json”.
c. En una nueva lista vacía almacena los objetos reconstruidos a partir del archivo
JSON.
d. Pedile al usuario una letra para buscar los contactos cuyo apellido comienza con esa
letra, y mostrá el resultado de la búsqueda por pantalla. 

'''

class Tester: 
    def almacenar_contactos(self, contactos):
        with open("contactos.json", "w") as file:
            json.dump([contacto.toDiccionario() for contacto in contactos], file)
            return contactos
    
    def cargar_contactos(self):
        with open("contactos.json", "r", encoding='UTF-8') as file:
            data = json.load(file)
            contactos = [Contacto.fromDiccionario(dicc) for dicc in data]
            return contactos

    def buscar_contactos_por_apellido(self, letra):
        contactos = self.cargar_contactos()
        resultados = []
        for contacto in contactos:
            if contacto.apellido.startswith(letra): # starts with: empieza con la letra ingresada
                resultados.append(contacto)
        return resultados
    
if __name__ == "__main__":
    tester = Tester()
    contactos = [
        # contactos:
        Contacto("Juan", "Perez", "123456789", "juanperez@gmail.com", "Calle Falsa 123"),
        Contacto("Juan", "Heguy", "123456789", "juanperez@gmail.com", "Calle Falsa 123"),
        Contacto("Juan", "Toridni", "123456789", "juanperez@gmail.com", "Calle Falsa 123")
    ]
    