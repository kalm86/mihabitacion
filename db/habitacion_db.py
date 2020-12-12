from typing import Dict
from pydantic import BaseModel

class Habitacion(BaseModel):
    Numero: int
    Descripcion: str
    TipoHabitacion: str

ListaHabitacion = Dict[str, Habitacion]
ListaHabitacion = {
    101: Habitacion(**{ "Numero":101,
                        "Descripcion":"Habitación doble con aire acondicionado.",
                            "TipoHabitacion":"Doble"}),
    102: Habitacion(**{ "Numero":102,
                        "Descripcion":"Habitación multiple con aire acondicionado.",
                        "TipoHabitacion":"Multiple"}),
    201: Habitacion(**{ "Numero":201,
                        "Descripcion":"Habitación doble con aire acondicionado y vista al mar.",
                        "TipoHabitacion":"Doble"}),
}

def ObtenerHabitacion(Numero: str):
    if Numero in ListaHabitacion.keys():
        return ListaHabitacion[Numero]
    else:
        return None

database_habitaciones = []

def GuardarHabitacion(Habitacion_db: ListaHabitacion):
    database_habitaciones.append(Habitacion_db)
    return Habitacion_db