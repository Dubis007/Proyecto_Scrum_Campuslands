import json
import os

BASE_DIR: str = os.path.dirname(os.path.abspath(__file__))
DATA_DIR: str = os.path.join(BASE_DIR, "datos")
RUTA_DEFAULT: str = os.path.join(DATA_DIR, "estudiantes.json")

def cargar_estudiantes(ruta_archivo: str = RUTA_DEFAULT) -> list[dict]:
    try:
        with open(ruta_archivo, encoding="utf-8") as archivo:
            contenido = archivo.read().strip()
        if not contenido:
            return []
        return json.loads(contenido)
    except FileNotFoundError:
        return []
    except IOError:
        print(f"Error al leer el archivo '{ruta_archivo}'.")
        return []
    except json.JSONDecodeError:
        return []


def guardar_estudiantes(estudiantes: list[dict], ruta_archivo: str = RUTA_DEFAULT) -> bool:
    try:
        os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(estudiantes, archivo, ensure_ascii=False, indent=4)
        return True
    except IOError:
        print(f"Error al guardar el archivo '{ruta_archivo}'.")
        return False


def validar_campos(datos: dict):
    for campo, valor in datos.items():
        if valor is None or not str(valor).strip():
            return False, f"El campo {campo} es obligatorio."
    return True, ""


def registrar_estudiante(
    documento: str,
    nombre: str,
    correo: str,
    programa: str,
    ruta_archivo: str = RUTA_DEFAULT,
):

    datos = {
        "documento": documento,
        "nombre": nombre,
        "correo": correo,
        "programa": programa,
    }

    valido, mensaje = validar_campos(datos)
    if not valido:
        return False, mensaje

    estudiante = {campo: str(valor).strip() for campo, valor in datos.items()}
    estudiantes = cargar_estudiantes(ruta_archivo)

    for registro in estudiantes:
        if str(registro.get("documento", "")).strip() == estudiante["documento"]:
            return False, "El estudiante ya está registrado."

    estudiantes.append(estudiante)
    guardar_estudiantes(estudiantes, ruta_archivo)
    return True, "Estudiante registrado correctamente."


def pedir_registro():
    print("\n--- Registrar estudiante ---")

    while True:
        documento = input("Documento de identidad : ")
        if not (7 <= len(documento.strip()) <= 10):
            print("El documento debe tener entre 7 y 10 dígitos.")
        elif not documento.strip():
            print("El documento no puede estar vacío.")
        elif not documento.strip().isdigit():
            print("El documento solo puede contener números.")

        else:
            break

    while True:
        nombre = input("Ingresar nombre completo: \n")
        if not nombre.strip():
            print("El nombre no puede estar vacío.")
        elif not nombre.strip().replace(" ", "").isalpha():
            print("El nombre solo puede contener letras.")
        else:
            break

    while True:
        correo = input("Ingresa el correo electrónico: \n")
        if not correo.strip():
            print("El correo no puede estar vacío.")
        elif "@" not in correo.strip():
            print("El correo debe contener '@'.")
        else:
            break

    while True:
        programa = input("Ingresar el programa academico: \n")
        if not programa.strip():
            print("El programa no puede estar vacío.")
        elif not programa.strip().replace(" ", "").isalpha():
            print("El programa solo puede contener letras.")
        else:
            break

    mensaje = registrar_estudiante(documento, nombre, correo, programa)
    print(f"\n{mensaje}")


def mostrar_estudiantes():
    print("\n--- Estudiantes registrados ---")
    estudiantes = cargar_estudiantes()

    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    for i, estudiante in enumerate(estudiantes, start=1):
        print(f"\nEstudiante {i}:")
        print(f"  Documento : {estudiante.get('documento')}")
        print(f"  Nombre    : {estudiante.get('nombre')}")
        print(f"  Correo    : {estudiante.get('correo')}")
        print(f"  Programa  : {estudiante.get('programa')}")
