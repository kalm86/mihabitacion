from pydantic import BaseModel

class UsuarioIngreso(BaseModel):
    Nick: str
    Contrasena: str

class UsuarioSalida(BaseModel):
    Nick: str
