# main.py

# Importar las clases necesarias
from departamento import Departamento
from quinta import Quinta
from propietario import Propietario

if __name__ == "__main__":
    # Crear instancias de Propietario
    propietario1 = Propietario("Juan Pérez", "12345678")
    propietario2 = Propietario("María García", "87654321")

    # Crear instancias de Departamento y Quinta
    departamento = Departamento(1, "Calle 123", propietario1.toString(), 80, 1, 5000.0, True)
    quinta = Quinta(2, "Ruta 456", propietario2.toString(), 500, 2, 1000)

    # Probar métodos de Departamento
    print("Departamento:")
    print(f"Costo de alquiler: {departamento.costoAlquiler(10000)}")  # Calcular y mostrar el costo de alquiler
    print(f"Precio de venta: {departamento.precioVenta(2000)}")  # Calcular y mostrar el precio de venta

    # Probar métodos de Quinta
    print("\nQuinta:")
    print(f"Costo de alquiler: {quinta.costoAlquiler(15000)}")  # Calcular y mostrar el costo de alquiler
    print(f"Precio de venta: {quinta.precioVenta(1500)}")  # Calcular y mostrar el precio de venta