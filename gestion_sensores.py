def ver_tipos_sensores():
    print("Mostrando tipos de sensores disponibles...")

def asignar_sensor():
    print("Asignando sensor a parcela...")

def eliminar_sensor():
    print("Eliminando sensor...")

def menu_sensores():
    while True:
        print("\n╔═══════════════════════════════════════════════════╗")
        print("║                GESTIÓN DE SENSORES                ║")
        print("╠═══════════════════════════════════════════════════╣")
        print("║ 1. Ver Tipos de Sensores                          ║")
        print("║ 2. Asignar Sensor a Parcela                       ║")
        print("║ 3. Eliminar Sensor                                ║")
        print("║ 4. Volver al menú principal                       ║")
        print("╚═══════════════════════════════════════════════════╝")
        
        sub_menu = input("Seleccione una opción de sensores: ")

        if sub_menu == "1":
            ver_tipos_sensores()
        elif sub_menu == "2":
            asignar_sensor()
        elif sub_menu == "3":
            eliminar_sensor()
        elif sub_menu == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")