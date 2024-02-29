# Una fábrica de instrumentos musicales posee una lista con todas sus sucursales.
# Cada sucursal tiene su nombre y una lista con todos los instrumentos a la venta.
# De cada uno de ellos se sabe su ID alfanumérico, su precio y su tipo
# (Percusión, Viento o Cuerda).

# Puntos a desarrollar
# 1)Desarrollar el diagrama de clases UML que modele lo enunciado y donde consten
# las clases con sus atributos, métodos y relaciones (los constructores pueden omitirse).

# 2) Crear un proyecto en Python que resuelva:
#     A) método listarInstrumentos que muestre en la consola todos los
#     datos de cada uno de los instrumentos. - DEVOLVEME TODOS LOS INSTRUMENTOS
#     B) método instrumentosPorTipo que devuelva una lista de 
#     instrumentos cuyo tipo coincida con el recibido por parámetro. ... DE CUERDAS (FILTRO)
#     C) método borrarInstrumento que reciba un ID y elimine el
#     instrumento asociado a tal ID de la sucursal donde se encuentre.
#     D) método porcInstrumentosPorTipo que reciba el nombre de una
#     sucursal y retorne los porcentajes de instrumentos por tipo que hay para tal sucursal.



from enum import Enum
from typing import List, Dict

class TipoInstrumento(Enum):
    PERCUSION = "Percusión"
    VIENTO = "Viento"
    CUERDA = "Cuerda"

class Instrumento:
    def __init__(self, id: str, precio: float, tipo: TipoInstrumento):
        self.id = id
        self.precio = precio
        self.tipo = tipo

    def __str__(self):
        return f"Instrumento ID: {self.id}, Precio: {self.precio}, Tipo: {self.tipo.value}"

class Sucursal:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.instrumentos: List[Instrumento] = []

    def listarInstrumentos(self):
        print(f"Instrumentos en la sucursal {self.nombre}:")
        for instrumento in self.instrumentos:
            print(instrumento)

    def instrumentosPorTipo(self, tipo: TipoInstrumento) -> List[Instrumento]:
        return [instrumento for instrumento in self.instrumentos if instrumento.tipo == tipo]

    def borrarInstrumento(self, id: str):
        self.instrumentos = [instrumento for instrumento in self.instrumentos if instrumento.id != id]

    def porcInstrumentosPorTipo(self) -> Dict[TipoInstrumento, float]:
        total_instrumentos = len(self.instrumentos)
        porcentajes = {}
        for tipo in TipoInstrumento:
            instrumentos_tipo = len([instrumento for instrumento in self.instrumentos if instrumento.tipo == tipo])
            porcentaje = (instrumentos_tipo / total_instrumentos) * 100 if total_instrumentos != 0 else 0
            porcentajes[tipo] = porcentaje
        return porcentajes

class Fabrica:
    def __init__(self):
        self.sucursales: List[Sucursal] = []

    def agregarSucursal(self, sucursal: Sucursal):
        self.sucursales.append(sucursal)

    def listarInstrumentos(self):
        print("Instrumentos en todas las sucursales:")
        for sucursal in self.sucursales:
            sucursal.listarInstrumentos()

    def instrumentosPorTipo(self, tipo: TipoInstrumento) -> List[Instrumento]:
        instrumentos = []
        for sucursal in self.sucursales:
            instrumentos.extend(sucursal.instrumentosPorTipo(tipo))
        return instrumentos

    def borrarInstrumento(self, id: str, nombre_sucursal: str):
        for sucursal in self.sucursales:
            if sucursal.nombre == nombre_sucursal:
                sucursal.borrarInstrumento(id)
                break

    def porcInstrumentosPorTipo(self) -> Dict[TipoInstrumento, float]:
        total_instrumentos = sum(len(sucursal.instrumentos) for sucursal in self.sucursales)
        porcentajes = {}
        for tipo in TipoInstrumento:
            instrumentos_tipo = sum(len(sucursal.instrumentosPorTipo(tipo)) for sucursal in self.sucursales)
            porcentaje = (instrumentos_tipo / total_instrumentos) * 100 if total_instrumentos != 0 else 0
            porcentajes[tipo] = porcentaje
        return porcentajes

# Ejemplo de uso
if __name__ == "__main__":
    fabrica = Fabrica()
    
    # Crear algunas sucursales y agregarlas a la fábrica
    sucursal1 = Sucursal("Sucursal Principal")
    sucursal2 = Sucursal("Sucursal Secundaria")
    fabrica.agregarSucursal(sucursal1)
    fabrica.agregarSucursal(sucursal2)

    # Agregar instrumentos a las sucursales
    instrumento1 = Instrumento("001", 100.0, TipoInstrumento.CUERDA)
    instrumento2 = Instrumento("002", 150.0, TipoInstrumento.VIENTO)
    instrumento3 = Instrumento("003", 80.0, TipoInstrumento.PERCUSION)
    sucursal1.instrumentos.extend([instrumento1, instrumento2])
    sucursal2.instrumentos.append(instrumento3)

    # Probar los métodos de la fábrica
    fabrica.listarInstrumentos()
    print("Instrumentos de tipo VIENTO en todas las sucursales:")
    print(fabrica.instrumentosPorTipo(TipoInstrumento.VIENTO))
    fabrica.borrarInstrumento("002", "Sucursal Principal")
    print("Después de borrar el instrumento 002 en Sucursal Principal:")
    fabrica.listarInstrumentos()
    print("Porcentajes de instrumentos por tipo en todas las sucursales:")
    print(fabrica.porcInstrumentosPorTipo())
