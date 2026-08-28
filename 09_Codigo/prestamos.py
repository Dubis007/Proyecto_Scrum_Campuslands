import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "datos")

os.makedirs(DATA_DIR, exist_ok=True)

EQUIPOS_JSON = os.path.join(DATA_DIR, 'equipos.json')
ESTUDIANTES_JSON = os.path.join(DATA_DIR, 'estudiantes.json')
PRESTAMOS_JSON = os.path.join(DATA_DIR, 'prestamos.json')

def cargar_datos_json(ruta):
    if not os.path.exists(ruta):
        return []
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            contenido = f.read().strip()
            if not contenido:
                return []
            return json.loads(contenido)
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

        prestamos_archivos = [p for p in prestamos if str(p.get('estado', '')).strip().upper() == 'ACTIVO']

        if not prestamos_archivos:
            print("No se encontraron equipos prestados Actualmete")
            return
        
        print("\n---BIENVENIDO A EQUIPOS ACTUALMENTE PRESTADOS ---")
        print("-" * 80)
        print(f"{'SERIAL/CODIGO':<10} | {'EQUIPO':<18} | {'ESTUDIANTE':<20} | {'FECHA PRESTAMO':<20}")
        print("-" * 80)

        for p in prestamos_archivos:
            cod_equipo = p.get('codigo_equipo') or p.get('serial') or 'N/A'
            doc_estudiante = p.get('documento_estudiante', 'N/A')
            fecha = p.get('fecha_prestamo', 'N/A')

            equipo_info = next((eq for eq in equipos if eq.get('serial') == cod_equipo or eq.get('codigo') == cod_equipo), None)
            detalle_equipo = f"{equipo_info['tipo']} {equipo_info['marca']}" if equipo_info else "Desconocido"

            estudiante_info = next((est for est in estudiantes if str(est.get('documento', '')).strip().upper() == str(doc_estudiante)), None)
            nombre_estudiante = estudiante_info.get('nombre', 'doc_estudiante') if estudiante_info else doc_estudiante

            print(f"{cod_equipo:<10} | {detalle_equipo:<18} | {nombre_estudiante:<20} | {fecha:<20}")

        print("-" * 80)

    except KeyError as e:
        print(f"\n[!] Error en la estructura de datos: Falta la clave {e}.")
    except Exception as e:
        print(f"\n[!] Ha ocurrido un error inesperado al consultar los préstamos: {e}")
