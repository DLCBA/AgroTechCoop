
print("    ___                  ______          __        ______                ")
print("   /   | ____ __________/_  __/__  _____/ /_      / ____/___  ____  ____ ")
print("  / /| |/ __ `/ ___/ __ \/ / / _ \/ ___/ __ \    / /   / __ \/ __ \/ __ \\")
print(" / ___ / /_/ / /  / /_/ / / /  __/ /__/ / / /   / /___/ /_/ / /_/ / /_/ /")
print("/_/  |_\__, /_/   \____/_/  \___/\___/_/ /_/    \____/\____/\____/ .___/ ")
print("      /____/                                                    /_/     ")
print("╔══════════════════════════════════════════════════════════════════════╗")
print("║         🌱 SISTEMA DE MONITOREO AGRÍCOLA - AGROTECH COOP 🌱          ║")
print("╠══════════════════════════════════════════════════════════════════════╣")
print("║                           Fecha: 11/05/2025                          ║")
print("╚══════════════════════════════════════════════════════════════════════╝")

# Menu principal, Si bien podemos generar todo el menu en una sola linea dentro
# del While, preferimos hacerlo linea a linea para una mejor visualizacón.

while True:
    print("\n╔═════════════════════════════════════════════════╗")
    print("║                  MENÚ PRINCIPAL                 ║")
    print("╠═════════════════════════════════════════════════╣")
    print("║ 1. Gestionar Parcelas                           ║")
    print("║ 2. Gestionar Sensores                           ║")
    print("║ 3. Registrar Mediciones                         ║")
    print("║ 4. Consultar Datos                              ║")
    print("║ 5. Visualizar Alertas                           ║")
    print("║ 6. Salir                                        ║")
    print("╚═════════════════════════════════════════════════╝")
    opcion = input("Seleccione una opción: ")

# Desde este punto generamos el acceso a cada submenu especifico y la salida
# correspondiente al menu principal. Esto se repite para cada opcion del menu.

    if opcion == "1":
        while True:
            print("\n╔═══════════════════════════════════════════════════╗")
            print("║                GESTIÓN DE PARCELAS                ║")
            print("╠═══════════════════════════════════════════════════╣")
            print("║ 1. Ver Parcelas                                   ║")
            print("║ 2. Agregar Parcela                                ║")
            print("║ 3. Modificar Parcela                              ║")
            print("║ 4. Eliminar Parcela                               ║")
            print("║ 5. Volver al menú principal                       ║")
            print("╚═══════════════════════════════════════════════════╝")
            sub_menu = input("Seleccione una opción de parcela: ")

            if sub_menu == "1":
                print("Mostrando parcelas registradas...")
            elif sub_menu == "2":
                print("Agregando nueva parcela...")
            elif sub_menu == "3":
                print("Modificando parcela existente...")
            elif sub_menu == "4":
                print("Eliminando parcela...")
            elif sub_menu == "5":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    elif opcion == "2":
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
                print("Mostrando tipos de sensores...")
            elif sub_menu == "2":
                print("Asignando sensor a parcela...")
            elif sub_menu == "3":
                print("Eliminando sensor...")
            elif sub_menu == "4":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    elif opcion == "3":
        while True:
            print("\n╔═══════════════════════════════════════════════════╗")
            print("║              REGISTRO DE MEDICIONES               ║")
            print("╠═══════════════════════════════════════════════════╣")
            print("║ 1. Registrar nueva medición                       ║")
            print("║ 2. Volver al menú principal                       ║")
            print("╚═══════════════════════════════════════════════════╝")
            sub_menu = input("Seleccione una opción: ")

            if sub_menu == "1":
                print("Registrando nueva medición...")
            elif sub_menu == "2":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    elif opcion == "4":
        while True:
            print("\n╔══════════════════════════════════════════════════╗")
            print("║                 CONSULTAR DATOS                  ║")
            print("╠══════════════════════════════════════════════════╣")
            print("║ 1. Ver últimas mediciones por parcela            ║")
            print("║ 2. Ver mediciones por tipo de sensor             ║")
            print("║ 3. Volver al menú principal                      ║")
            print("╚══════════════════════════════════════════════════╝")
            sub_menu = input("Seleccione una opción: ")

            if sub_menu == "1":
                print("Consultando últimas mediciones por parcela...")
            elif sub_menu == "2":
                print("Consultando mediciones por tipo de sensor...")
            elif sub_menu == "3":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    elif opcion == "5":
        while True:
            print("\n╔═══════════════════════════════════════════════════╗")
            print("║                ALERTAS DEL SISTEMA                ║")
            print("╠═══════════════════════════════════════════════════╣")
            print("║ 1. Ver alertas activas por parcela                ║")
            print("║ 2. Ver alertas por tipo de sensor                 ║")
            print("║ 3. Ver historial de alertas                       ║")
            print("║ 4. Volver al menú principal                       ║")
            print("╚═══════════════════════════════════════════════════╝")
            sub_menu = input("Seleccione una opción de alertas: ")
            if sub_menu == "1":
                print("Mostrando alertas activas por parcela...")
            elif sub_menu == "2":
                print("Mostrando alertas por tipo de sensor...")
            elif sub_menu == "3":
                print("Mostrando historial completo de alertas...")
            elif sub_menu == "4":
                break
            else:
                print("Opción inválida. Intente nuevamente.")

    elif opcion == "6":
        print("Saliendo del sistema.")
        print("\n╔═════════════════════════════════════════════╗")
        print("║    🌱 Gracias por usar AgroTech Coop 🌱    ║")
        print("║            ¡Hasta la próxima!               ║")
        print("╚═════════════════════════════════════════════╝")
        break

    else:
        print("Opción inválida. Intente nuevamente.")