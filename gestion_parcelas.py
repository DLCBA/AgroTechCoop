# Diccionario para almacenar parcelas
parcelas = {}

def ver_parcelas():
    print("\n--- Parcelas Registradas ---")
    if not parcelas:
        print("No hay parcelas registradas")
    else:
        print("ID  | Nombre           | Ubicación      | Latitud    | Longitud   | Tamaño (ha) | Cultivo")
        print("-" * 80)
        for id, datos in parcelas.items():
            print(f"{id:3} | {datos['nombre'][:15]:15} | {datos['ubicacion'][:15]:15} | "
                  f"{datos['latitud']:10} | {datos['longitud']:10} | "
                  f"{datos['tamano_hectareas']:11} | {datos['tipo_cultivo']}")

def agregar_parcela():
    print("\n--- Agregar Nueva Parcela ---")
    id = input("Ingrese ID de la parcela: ")
    nombre = input("Nombre de la parcela: ")
    ubicacion = input("Ubicación: ")
    latitud = input("Latitud: ")
    longitud = input("Longitud: ")
    tamano_hectareas = input("Tamaño en hectáreas: ")
    tipo_cultivo = input("Tipo de cultivo: ")
    
    parcelas[id] = {
        'nombre': nombre,
        'ubicacion': ubicacion,
        'latitud': latitud,
        'longitud': longitud,
        'tamano_hectareas': tamano_hectareas,
        'tipo_cultivo': tipo_cultivo
    }
    print(f"Parcela {nombre} agregada correctamente!")

def modificar_parcela():
    print("\n--- Modificar Parcela ---")
    id = input("Ingrese ID de la parcela a modificar: ")
    
    if id in parcelas:
        print("Deje en blanco los campos que no desea modificar")
        nombre = input(f"Nuevo nombre ({parcelas[id]['nombre']}): ") or parcelas[id]['nombre']
        ubicacion = input(f"Nueva ubicación ({parcelas[id]['ubicacion']}): ") or parcelas[id]['ubicacion']
        latitud = input(f"Nueva latitud ({parcelas[id]['latitud']}): ") or parcelas[id]['latitud']
        longitud = input(f"Nueva longitud ({parcelas[id]['longitud']}): ") or parcelas[id]['longitud']
        tamano_hectareas = input(f"Nuevo tamaño en hectáreas ({parcelas[id]['tamano_hectareas']}): ") or parcelas[id]['tamano_hectareas']
        tipo_cultivo = input(f"Nuevo tipo de cultivo ({parcelas[id]['tipo_cultivo']}): ") or parcelas[id]['tipo_cultivo']
        
        parcelas[id] = {
            'nombre': nombre,
            'ubicacion': ubicacion,
            'latitud': latitud,
            'longitud': longitud,
            'tamano_hectareas': tamano_hectareas,
            'tipo_cultivo': tipo_cultivo
        }
        print("Parcela actualizada correctamente")
    else:
        print("Error: Parcela no encontrada")

def eliminar_parcela():
    print("\n--- Eliminar Parcela ---")
    id = input("Ingrese ID de la parcela a eliminar: ")
    
    if id in parcelas:
        confirmar = input(f"¿Está seguro de eliminar {parcelas[id]['nombre']}? (s/n): ")
        if confirmar.lower() == 's':
            del parcelas[id]
            print("Parcela eliminada correctamente")
    else:
        print("Error: Parcela no encontrada")

def menu_parcelas():
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
        
        sub_menu = input("Seleccione una opción: ")

        if sub_menu == "1":
            ver_parcelas()
        elif sub_menu == "2":
            agregar_parcela()
        elif sub_menu == "3":
            modificar_parcela()
        elif sub_menu == "4":
            eliminar_parcela()
        elif sub_menu == "5":
            break
        else:
            print("Opción inválida. Intente nuevamente.")