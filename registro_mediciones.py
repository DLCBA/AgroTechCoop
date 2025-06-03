def registrar_medicion():
    print("Registrando nueva medición...")

def menu_mediciones():
    while True:
        print("\n╔═══════════════════════════════════════════════════╗")
        print("║              REGISTRO DE MEDICIONES               ║")
        print("╠═══════════════════════════════════════════════════╣")
        print("║ 1. Registrar nueva medición                       ║")
        print("║ 2. Volver al menú principal                       ║")
        print("╚═══════════════════════════════════════════════════╝")
        
        sub_menu = input("Seleccione una opción: ")

        if sub_menu == "1":
            registrar_medicion()
        elif sub_menu == "2":
            break
        else:
            print("Opción inválida. Intente nuevamente.")