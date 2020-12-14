# Usuario
from db.usuario_db import Usuario
from db.usuario_db import ObtenerUsuario
from modelos.usuario_modelo import UsuarioIngreso, UsuarioSalida

# Habitacion
from db.habitacion_db import Habitacion
from db.habitacion_db import ObtenerHabitacion, GuardarHabitacion
from modelos.habitacion_modelo import CrearHabitacion, ActualizarHabitacion, BorrarHabitacion, ConsultarHabitacion

# Otros
import datetime
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()
origins = [
"http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
"http://localhost", "http://localhost:8080",
]

api.add_middleware(
CORSMiddleware, allow_origins=origins,
allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

@api.post("/usuario/autenticacion/")
async def Autenticacion(UsuarioIngreso: UsuarioIngreso):

    UsuarioDB = ObtenerUsuario(UsuarioIngreso.Nick)

    if UsuarioDB == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if UsuarioDB.Contrasena != UsuarioIngreso.Contrasena:
        return  {"Autenticado": False}

    return  {"Autenticado": True}

@api.get("/usuario/{Nick}")
async def Consulta_Usuario(Nick: str):

    UsuarioDB = ObtenerUsuario(Nick)

    if UsuarioDB == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    Salida = UsuarioSalida(**UsuarioDB.dict())

    return  Salida

@api.put("/habitacion/crear/")
async def Crear_Habitacion(HabitacionBlanco: CrearHabitacion):
    NuevaHabitacion = Habitacion(**HabitacionBlanco.dict())
    NuevaHabitacion = GuardarHabitacion(HabitacionBlanco)

    ObtenerHabitacion = ConsultarHabitacion(**HabitacionBlanco.dict())

    return  ObtenerHabitacion

@api.get("/habitacion/{Numero}")
async def Consulta_Habitacion(Numero: int):

    HabitacionDB = ObtenerHabitacion(Numero)

    if HabitacionDB == None:
        raise HTTPException(status_code=404, detail="No existe esta habitación.")

    ConsultarHabitacion = Habitacion(**HabitacionDB.dict())

    return  ConsultarHabitacion