def alertas_activas():
    print("Mostrando alertas activas por parcela...")

def alertas_por_sensor():
    print("Mostrando alertas por tipo de sensor...")

def historial_alertas():
    print("Mostrando historial completo de alertas...")

def menu_alertas():
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
            alertas_activas()
        elif sub_menu == "2":
            alertas_por_sensor()
        elif sub_menu == "3":
            historial_alertas()
        elif sub_menu == "4":
            break
        else:
            print("Opción inválida. Intente nuevamente.")