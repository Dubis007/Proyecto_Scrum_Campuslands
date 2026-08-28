import json
import os
from datetime import datetime

BASE_DIR : str = os.path.dirname(os.path.abspath(__file__))
DATA_DIR : str = os.path.join(BASE_DIR, "datos")
RUTA_ESTUDIANTES : str = os.path.join(DATA_DIR, "estudiantes.json")
RUTA_EQUIPOS : str = os.path.join(DATA_DIR, "equipos.json")
RUTA_PRESTAMOS : str = os.path.join(DATA_DIR, "prestamos.json")


def cargar_datos(ruta_archivo):
    try:
        with open(ruta_archivo, encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
        return json.loads(contenido) if contenido else []
    except (FileNotFoundError, json.JSONDecodeError, IOError):
        return []


def guardar_datos(datos, ruta_archivo) -> bool:
    try:
        os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=4)
        return True
    except IOError:
        print(f"Error al guardar el archivo '{ruta_archivo}'.")
        return False


def registrar_prestamo(
    documento,
    codigo_equipo,
    estudiantes=RUTA_ESTUDIANTES,
    equipos=RUTA_EQUIPOS,
    prestamos=RUTA_PRESTAMOS,
):
    documento = str(documento).strip()
    codigo_equipo = str(codigo_equipo).strip().upper()

    lista_estudiantes = cargar_datos(estudiantes)
    estudiante_encontrado = None
    for registro in lista_estudiantes:
        if str(registro.get("documento", "")).strip() == documento:
            estudiante_encontrado = registro
            break
    if estudiante_encontrado is None:
        return False, "El estudiante no está registrado."

    lista_equipos = cargar_datos(equipos)
    equipo_encontrado = None
    for registro in lista_equipos:
        serial = str(registro.get("serial", registro.get("codigo", ""))).strip().upper()
        if serial == codigo_equipo:
            equipo_encontrado = registro
            break
    if equipo_encontrado is None:
        return False, "El equipo no está registrado."

    if str(equipo_encontrado.get("estado", "")).strip().upper() != "DISPONIBLE":
        return False, "El equipo no está disponible."

    lista_prestamos = cargar_datos(prestamos)
    ids = [p.get("id", 0) for p in lista_prestamos]
    nuevo_id = max(ids, default=0) + 1
    nuevo_prestamo = {
        "id": nuevo_id,
        "fecha_prestamo": datetime.now().strftime("%Y-%m-%d"),
        "documento_estudiante": documento,
        "codigo_equipo": codigo_equipo,
        "estado": "ACTIVO",
    }

    equipo_encontrado["estado"] = "PRESTADO"
    lista_prestamos.append(nuevo_prestamo)
    guardar_datos(lista_prestamos, prestamos)
    guardar_datos(lista_equipos, equipos)
    return True, "Préstamo creado correctamente."



def pedir_prestamo():
    print("\n--- Registrar préstamo ---")

    while True:
        documento = input("Documento del estudiante : ")
        if not documento.strip():
            print("El documento no puede estar vacío.")
        elif not documento.strip().isdigit():
            print("El documento solo puede contener números.")
        elif not (7 <= len(documento.strip()) <= 10):
            print("El documento debe tener entre 7 y 10 dígitos.")
        else:
            break

    while True:
        codigo_equipo = input("Código del equipo         : ")
        if not codigo_equipo.strip():
            print("El código del equipo no puede estar vacío.")
        elif not codigo_equipo.strip().isalnum():
            print("El código del equipo solo puede contener letras y números.")
        else:
            break
        
    mensaje = registrar_prestamo(documento, codigo_equipo)
    print(f"\n{mensaje}")
