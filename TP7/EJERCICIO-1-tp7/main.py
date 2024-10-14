# main.py 

from aseguradora import Aseguradora
from polizaInmueble import PolizaInmueble
from polizaInmuebleEscolar import PolizaInmuebleEscolar

def main():
    # Prueba de la clase Aseguradora
    print("Prueba de Aseguradora:")
    aseguradora = Aseguradora()
    print(f"¿Hay pólizas? {aseguradora.hayPolizas()}")
    print(f"Costo total: {aseguradora.costoTotal()}")

    # Prueba de la clase PolizaInmueble
    print("\nPrueba de PolizaInmueble:")
    poliza = PolizaInmueble(1, 1000.0, 500.0, 200.0)
    print(f"Póliza: {poliza}")
    print(f"Costo de la póliza: {poliza.costoPoliza()}")

    # Prueba de la clase PolizaInmuebleEscolar
    print("\nPrueba de PolizaInmuebleEscolar:")
    poliza_escolar = PolizaInmuebleEscolar(2, 2000.0, 1000.0, 500.0, 100, 5000.0, 3000.0, 50.0)
    print(f"Póliza escolar: {poliza_escolar}")
    print(f"Costo de la póliza escolar: {poliza_escolar.costoPoliza()}")

    # Prueba de los nuevos métodos de Aseguradora
    print("\nPrueba de los nuevos métodos de Aseguradora:")
    aseguradora.insertar(poliza)
    aseguradora.insertar(poliza_escolar)
    print(f"¿Hay pólizas después de insertar? {aseguradora.hayPolizas()}")
    print(f"Costo total después de insertar: {aseguradora.costoTotal()}")
    print(f"¿Existe la póliza 1? {aseguradora.existePoliza(poliza)}")
    print(f"¿Existe la póliza escolar? {aseguradora.existePoliza(poliza_escolar)}")

    # Prueba de eliminar póliza
    aseguradora.eliminar(poliza)
    print(f"¿Existe la póliza 1 después de eliminar? {aseguradora.existePoliza(poliza)}")

    # Prueba de esIgual
    otra_aseguradora = Aseguradora()
    otra_aseguradora.insertar(poliza_escolar)
    print(f"¿Son iguales las aseguradoras? {aseguradora.esIgual(otra_aseguradora)}")

    # Prueba de los nuevos métodos de PolizaInmueble y PolizaInmuebleEscolar
    print("\nPrueba de los nuevos métodos de PolizaInmueble y PolizaInmuebleEscolar:")
    poliza.setNumero(3)
    print(f"Nuevo número de póliza: {poliza.getNumero()}")
    poliza.setIncendio(1500.0)
    print(f"Nuevo monto de incendio: {poliza.getIncendio()}")

    poliza_escolar.setCantPersonas(150)
    print(f"Nueva cantidad de personas: {poliza_escolar.getCantPersonas()}")
    poliza_escolar.setMontoEquipamiento(6000.0)
    print(f"Nuevo monto de equipamiento: {poliza_escolar.getMontoEquipamiento()}")

if __name__ == "__main__":
    main()

    
    
    
