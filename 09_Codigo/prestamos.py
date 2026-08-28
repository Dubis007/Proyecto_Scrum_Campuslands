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

    lista_est = cargar_datos(RUTA_ESTUDIANTES)
    if not lista_est:
        print("\nNo hay estudiantes registrados. Registre un estudiante primero.")
        return

    print("\nEstudiantes registrados:")
    print("-" * 58)
    print(f"  {'DOCUMENTO':<12} | {'NOMBRE':<22} | PROGRAMA")
    print("-" * 58)
    for est in lista_est:
        print(f"  {est.get('documento', 'N/A'):<12} | "
              f"{est.get('nombre', 'N/A'):<22} | "
              f"{est.get('programa', 'N/A')}")
    print("-" * 58)

    while True:
        documento = input("\nDocumento del estudiante : ")
        if not documento.strip():
            print("El documento no puede estar vacío.")
        elif not documento.strip().isdigit():
            print("El documento solo puede contener números.")
        elif not (7 <= len(documento.strip()) <= 10):
            print("El documento debe tener entre 7 y 10 dígitos.")
        else:
            break

    lista_eq = cargar_datos(RUTA_EQUIPOS)
    disponibles = []
    for eq in lista_eq:
        if str(eq.get("estado", "")).strip().upper() == "DISPONIBLE":
            disponibles.append(eq)

    if not disponibles:
        print("\nNo hay equipos disponibles en este momento.")
        return

    print("\nEquipos disponibles:")
    print("-" * 58)
    print(f"  {'SERIAL':<10} | {'TIPO':<12} | {'MARCA':<10} | MODELO")
    print("-" * 58)
    for eq in disponibles:
        serial = eq.get("serial") or eq.get("codigo") or "N/A"
        print(f"  {serial:<10} | "
              f"{eq.get('tipo', 'N/A'):<12} | "
              f"{eq.get('marca', 'N/A'):<10} | "
              f"{eq.get('modelo', 'N/A')}")
    print("-" * 58)

    while True:
        codigo_equipo = input("\nCódigo del equipo         : ")
        if not codigo_equipo.strip():
            print("El código del equipo no puede estar vacío.")
        elif not codigo_equipo.strip().isalnum():
            print("El código del equipo solo puede contener letras y números.")
        else:
            break

    mensaje = registrar_prestamo(documento, codigo_equipo)
    print(f"\n{mensaje}")


def cargar_datos_json(ruta):
    if not os.path.exists(ruta):
        return []
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"[!] Error: El archivo '{ruta}' tiene un formato inválido o está dañado.")
        return []
    except Exception as e:
        print(f"[!] Error inesperado al leer '{ruta}': {e}")
        return []

def consultar_equipos_prestados():
    try:
        prestamos = cargar_datos_json(RUTA_PRESTAMOS)
        estudiantes = cargar_datos_json(RUTA_ESTUDIANTES)
        equipos = cargar_datos_json(RUTA_EQUIPOS)

        prestamos_archivos = [p for p in prestamos if p.get('estado') == 'activo']

        if not prestamos_archivos:
            print("No se encontraron equipos prestados Actualmete")
            return
        
        print("\n---BIENVENIDO A EQUIPOS ACTUALMENTE PRESTADOS ---")
        print("-" * 80)
        print(f"{'CÓDIGO':<10} | {'EQUIPO':<18} | {'ESTUDIANTE':<20} | {'FECHA PRÉSTAMO':<20}")
        print("-" * 80)

        for p in prestamos_archivos:
            cod_equipo = p.get('codigo_equipo', 'N/A')
            doc_estudiante = p.get('documento_estudiante', 'N/A')
            fecha = p.get('fecha_prestamo', 'N/A')

            equipo_info = next((eq for eq in equipos if eq.get('codigo') == cod_equipo), None)
            detalle_equipo = f"{equipo_info['tipo']} {equipo_info['marca']}" if equipo_info else "Desconocido"

            estudiante_info = next((est for est in estudiantes if est.get('documento') == doc_estudiante), None)
            nombre_estudiante = estudiante_info.get('nombre', 'Desconocido') if estudiante_info else doc_estudiante

            print(f"{cod_equipo:<10} | {detalle_equipo:<18} | {nombre_estudiante:<20} | {fecha:<20}")

        print("-" * 80)

    except KeyError as e:
        print(f"\n[!] Error en la estructura de datos: Falta la clave {e}.")
    except Exception as e:
        print(f"\n[!] Ha ocurrido un error inesperado al consultar los préstamos: {e}")
