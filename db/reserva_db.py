from typing import Dict
from pydantic import BaseModel
import datetime

class Reserva(BaseModel):
    Usuario: str
    Fecha: datetime.date
    Habitacion: str

ListaReserva = Dict[str, Reserva]
ListaReserva = {
    "kalm": Reserva(**{ "Nick":"kalm",
                        "Contrasena":"12345"}),
}

def ObtenerUsuario(Nick: str):
    if Nick in ListaUsuario.keys():
        return ListaUsuario[Nick]
    else:
        return None