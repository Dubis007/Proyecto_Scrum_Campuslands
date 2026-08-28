import json
import os
from datetime import datetime

EQUIPOS_JSON = 'datos/equipos.json'

def cargar_equipos():
    if not os.path.exists(EQUIPOS_JSON):
        return[]
    try:
        with open(EQUIPOS_JSON, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError: 
        print("Error: El archivo 'equipos.json' está dañado o tiene un formato inválido.")
        return []
    except Exception as e: 
        print(f"Error inesperado al leer el archivo de equipos: {e}")
        return []

def consultar_equipos(solo_disponibles=False):
    try:
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
    except KeyError as e:
        print(f"\n[!] Error de estructura: Falta la clave esperada {e} en uno de los registros.")
    except Exception as e:
        print(f"\n[!] Ha ocurrido un error inesperado al consultar los equipos: {e}")

def registrar_nuevo_equipo():
    print(" Bienvenido al sistema de registro de equipos\n")
    
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_json = os.path.join(directorio_actual, "datos", "equipos.json")
    
    directorio = os.path.dirname(ruta_json)
    if directorio and not os.path.exists(directorio):
        try:
            os.makedirs(directorio, exist_ok=True)
        except Exception as e:
            print(f"Error al crear los directorios: {e}\n")
    
    equipos = []
    if os.path.exists(ruta_json):
        try:
            with open(ruta_json, "r", encoding="utf-8") as archivo:
                equipos = json.load(archivo)
        except Exception as e:
            print(f"Error al leer el archivo JSON: {e}\n")
            return []
            
    # Autoincremental id
    if len(equipos) == 0:
        nuevo_id = 1
    else:
        try:
            nuevo_id = max(eq.get("id", 0) for eq in equipos) + 1
        except Exception:
            nuevo_id = len(equipos) + 1

    try:
        # Ingreso de serial estilo placa de carro
        while True:
            try:
                serial_input = input("Ingrese el serial del equipo (3 letras y 3 números, ej: LNV001): \n").strip()
                if not serial_input:
                    print("El campo no puede estar vacío. Intente de nuevo.\n")
                    continue
                    
                if len(serial_input) == 6:
                    # revision letras y numeros
                    letras = serial_input[:3].upper()
                    numeros = serial_input[3:]
                    
                    if letras.isalpha() and numeros.isdigit():
                        serial_f = letras + numeros
                        
                        # verificar duplicados
                        es_duplicado = False
                        for eq in equipos:
                            if eq.get("serial") == serial_f:
                                es_duplicado = True
                                break
                        
                        if es_duplicado:
                            print(f"Error: El serial {serial_f} ya está registrado en el sistema. Ingrese uno diferente.\n")
                        else:
                            print(f"Serial válido: {serial_f}\n")
                            break
                    else:
                        print("Formato incorrecto. Recuerde: 3 letras iniciales y 3 números finales (ej: ABC123).\n")
                else:
                    print(f"Longitud inválida ({len(serial_input)}). Debe tener exactamente 6 caracteres.\n")
            except Exception as e:
                print(f"Error inesperado procesando el serial: {e}. Reintentando...\n")

        # Seleccionar tipo de equipo
        while True:
            try:
                tipo = input("Ingrese el tipo de equipo (PORTATIL, TABLET o PROYECTOR): \n").strip().upper()
                if tipo in ["PORTATIL", "TABLET", "PROYECTOR"]:
                    print(f"Tipo válido: {tipo}\n")
                    break
                else:
                    print("Tipo no válido. Ingrese únicamente PORTATIL, TABLET o PROYECTOR.\n")
            except Exception as e:
                print(f"Error procesando el tipo de equipo: {e}. Reintentando...\n")

        # Ingresar marca
        while True:
            try:
                marca = input("Ingrese la marca del equipo (ej: Lenovo, HP): \n").strip().upper()
                if not marca:
                    print("El campo no puede estar vacío. Intente de nuevo.\n")
                    continue
                print(f"Marca válida: {marca}\n")
                break
            except Exception as e:
                print(f"Error procesando la marca: {e}. Reintentando...\n")

        # Validar Modelo
        while True:
            try:
                modelo = input("Ingrese el modelo del equipo (ej: LOQ, THINKPAD): \n").strip().upper()
                if not modelo:
                    print("El campo no puede estar vacío. Intente de nuevo.\n")
                    continue
                print(f"Modelo válido: {modelo}\n")
                break
            except Exception as e:
                print(f"Error procesando el modelo: {e}. Reintentando...\n")

        # Estado de el equipo y fecha actual 
        estado = "DISPONIBLE"
        fecha_actual = datetime.now().strftime("%Y-%m-%d")

        # Nuevo equipo en diccionario JSON
        equipo_nuevo = {
            "id": nuevo_id,
            "serial": serial_f,
            "tipo": tipo,
            "marca": marca,
            "modelo": modelo,
            "estado": estado,
            "fecha_registro": fecha_actual
        }

        # Guardar en el JSON
        equipos.append(equipo_nuevo)
        
        with open(ruta_json, "w", encoding="utf-8") as archivo:
            json.dump(equipos, archivo, indent=4, ensure_ascii=False)
            
        print(f"¡Éxito! El equipo {tipo} {marca} {modelo} (Serial: {serial_f}) fue registrado correctamente.\n")

    except Exception as e:
        print(f"Ocurrió un error inesperado durante el registro general: {e}")
        

def menu_equipos():

    while True:

        print("------MÓDULO DE GESTIÓN DE EQUIPOS------")
        print("Este módulo administra el inventario físico.")
        print("Permite registrar PORTÁTILES, TABLETS o PROYECTORES,")
        print("asignando ID, estado y fecha de forma automática.")
        print("MENÚ DE OPCIONES")
        print("1. Registrar un nuevo equipo")
        print("2. Regresar al menú principal")
    
        try:
            opcion = input("Seleccione la opción deseada (1 o 2): \n").strip()
            
            if opcion == "1":
                registrar_nuevo_equipo()
            elif opcion == "2":
                print("Saliendo del módulo de gestión de equipos...\n")
                return
            else:
                print("Opción incorrecta. Por favor digite 1 o 2.\n")
        except Exception as e:
            print(f"Error inesperado en el menú: {e}\n")
