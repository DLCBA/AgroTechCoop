import gestion_parcelas
import gestion_sensores
import registro_mediciones
import consulta_datos
import alertas_sistema
from datetime import datetime

fecha_actual = datetime.now().strftime("%d/%m/%Y")

print("    ___                  ______          __        ______                ")
print("   /   | ____ __________/_  __/__  _____/ /_      / ____/___  ____  ____ ")
print("  / /| |/ __ `/ ___/ __ \/ / / _ \/ ___/ __ \    / /   / __ \/ __ \/ __ \\")
print(" / ___ / /_/ / /  / /_/ / / /  __/ /__/ / / /   / /___/ /_/ / /_/ / /_/ /")
print("/_/  |_\__, /_/   \____/_/  \___/\___/_/ /_/    \____/\____/\____/ .___/ ")
print("      /____/                                                    /_/     ")
print("╔══════════════════════════════════════════════════════════════════════╗")
print("║         🌱 SISTEMA DE MONITOREO AGRÍCOLA - AGROTECH COOP 🌱         ║")
print("╠══════════════════════════════════════════════════════════════════════╣")
print(f"║                          Fecha: {fecha_actual}                           ║")
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

    if opcion == "1":
        gestion_parcelas.menu_parcelas()

    elif opcion == "2":
        gestion_sensores.menu_sensores()

    elif opcion == "3":
        registro_mediciones.menu_mediciones()

    elif opcion == "4":
        consulta_datos.menu_consultas()

    elif opcion == "5":
        alertas_sistema.menu_alertas()

    elif opcion == "6":
        print("Saliendo del sistema.")
        print("\n╔═════════════════════════════════════════════╗")
        print("║    🌱 Gracias por usar AgroTech Coop 🌱    ║")
        print("║            ¡Hasta la próxima!               ║")
        print("╚═════════════════════════════════════════════╝")
        break

    else:
        print("Opción inválida. Intente nuevamente.")