import json
import os 

EQUIPOS_JSON = 'datos/equipos.py'

def cargar_equipos():
    if not os.path.exists(EQUIPOS_JSON):
        return[]
    try:
        with open(EQUIPOS_JSON, 'r', enconding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def consultar_equipos(solo_disponibles=False):
    equipos = cargar_equipos()

    if not equipos:
        print("\nNo existen equipos registrados en el sistema")
        return
    
    if solo_disponibles:
        equipos_a_mostrar = [equi for equi in equipos if equi.get('estado') == 'disponible']
        titulo = "______LISTA DE EQUIPOS DISPONIBLES______"
    else : 
        equipos_a_mostrar = equipos
        titulo = "____INVENTARIO GENERAL DE EQUIPOS____"

    if not equipos_a_mostrar:
        print("\nNo existen equipos registrados actualmente.")
        return

    print(f"\n{titulo}")
    print("-" * 65)
    print(f"{'CÓDIGO':<10} | {'TIPO':<12} | {'MARCA':<12} | {'MODELO':<12} | {'ESTADO':<10}")
    print("-" * 65)

    for equi in equipos_a_mostrar:
        codigo = equi.get('codigo', 'N/A')
        tipo = equi.get('tipo', 'N/A')
        marca = equi.get('marca', 'N/A')
        modelo = equi.get('modelo', 'N/A')
        estado = equi.get('estado', 'N/A')

        print(f"{codigo:<10} | {tipo:<12} | {marca:<12} | {modelo:<12} | {estado:<10}")

    print("-" * 65)                   