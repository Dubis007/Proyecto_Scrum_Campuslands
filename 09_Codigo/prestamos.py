import json
import os

EQUIPOS_JSON = 'datos/equipos.json'
ESTUDIANTES_JSON = 'datos/estudiantes.json'
PRESTAMOS_JSON = 'datos/prestamos.json'

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
        prestamos = cargar_datos_json(PRESTAMOS_JSON)
        estudiantes = cargar_datos_json(ESTUDIANTES_JSON)
        equipos = cargar_datos_json(EQUIPOS_JSON)

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