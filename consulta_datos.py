def mediciones_por_parcela():
    print("Consultando últimas mediciones por parcela...")

def mediciones_por_sensor():
    print("Consultando mediciones por tipo de sensor...")

def menu_consultas():
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
            mediciones_por_parcela()
        elif sub_menu == "2":
            mediciones_por_sensor()
        elif sub_menu == "3":
            break
        else:
            print("Opción inválida. Intente nuevamente.")