from pydantic import BaseModel

class CrearHabitacion(BaseModel):
    Numero: int
    Descripcion: str
    TipoHabitacion: str

class ActualizarHabitacion(BaseModel):
    Numero: int
    Descripcion: str
    TipoHabitacion: str

class BorrarHabitacion(BaseModel):
    Numero: int
    Descripcion: str
    TipoHabitacion: str

class ConsultarHabitacion(BaseModel):
    Numero: int
    Descripcion: str
    TipoHabitacion: str
