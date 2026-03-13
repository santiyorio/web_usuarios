from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()


class Usuario(BaseModel):
    nombre: str
    edad: int


def get_db():
    conn = sqlite3.connect("database.db")
    return conn


@app.get("/crear")
def crear():

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        edad INTEGER
    )
    """)

    conn.commit()
    conn.close()

    return {"msg": "tabla creada"}


@app.get("/usuarios")
def usuarios():

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")

    datos = cursor.fetchall()

    conn.close()

    return datos


@app.post("/agregar")
async def agregar(usuario: Usuario):

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO usuarios (nombre, edad) VALUES (?, ?)",
        (usuario.nombre, usuario.edad)
    )

    conn.commit()
    conn.close()

    return {"msg": "ok"}