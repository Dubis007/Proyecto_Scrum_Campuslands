from equipos import consultar_equipos
from prestamos import consultar_equipos_prestados
from estudiantes import pedir_registro, mostrar_estudiantes

def menu_principal():
    while True:
        print("\n____BIENVENIDO A SISTEMA DE PRÉSTAMOS____")
        print("1. Consultar todos los equipos")
        print("2. Consultar solo equipos disponibles")
        print("3. Registrar estudiante")
        print("4. Mostrar estudiantes registrados")
        print("7. Consultar equipos prestados")
        print("0. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            consultar_equipos(solo_disponibles=False)
        elif opcion == "2":
                consultar_equipos(solo_disponibles=True)
        elif opcion == "3":
                pedir_registro()
        elif opcion == "4":        
                mostrar_estudiantes()
        elif opcion == "7":
             consultar_equipos_prestados()        
        elif opcion == "0":
             break
        else:
             print("La opción ingresada es Inválida. ")

if __name__ == "__main__":
  menu_principal()           