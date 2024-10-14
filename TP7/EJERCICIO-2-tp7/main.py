# main.py 

# Importación de las clases
from departamento import Departamento
from quinta import Quinta

# tester

if __name__ == "__main__":
    # Crear instancias de Departamento y Quinta
    departamento = Departamento(1, "Calle 123", "Juan Pérez", 80, 1, 5000.0, True)
    quinta = Quinta(2, "Ruta 456", "María García", 500, 2, 1000)

    # Probar métodos de Departamento
    print("Departamento:")
    print(f"Costo de alquiler: {departamento.costoAlquiler(10000)}")
    print(f"Precio de venta: {departamento.precioVenta(2000)}")

    # Probar métodos de Quinta
    print("\nQuinta:")
    print(f"Costo de alquiler: {quinta.costoAlquiler(15000)}")
    print(f"Precio de venta: {quinta.precioVenta(1500)}")

