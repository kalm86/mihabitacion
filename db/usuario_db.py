from typing import Dict
from pydantic import BaseModel

class Usuario(BaseModel):
    Nick: str
    Contrasena: str

ListaUsuario = Dict[str, Usuario]
ListaUsuario = {
    "kalm": Usuario(**{ "Nick":"kalm",
                        "Contrasena":"12345"}),
}

def ObtenerUsuario(Nick: str):
    if Nick in ListaUsuario.keys():
        return ListaUsuario[Nick]
    else:
        return None