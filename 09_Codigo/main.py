from equipos import consultar_equipos

def menu_principal():
    while True:
        print("\n____ SISTEMA DE PRÉSTAMOS____")
        print("1. Consultar todos los equipos")
        print("2. Consultar solo equipos disponibles")
        print("0. salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            consultar_equipos(solo_disponibles=False)
        elif opcion == "2":
                consultar_equipos(solo_disponibles=True)
        elif opcion == "0":
             break
        else:
             print("La opción ingresada es Inválida. ")

if __name__ == "__main__":
  menu_principal()           