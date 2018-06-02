# Programa que carga equipos y puntajes y arma tabla de posiciones

def Cargar_Equipos(equipos):
    """Carga los nombres e inicializa los equipos"""
    nombre = input("Ingrese el nombre del equipo, q para terminar: ")
    if nombre == 'q' or 'Q':
        return
    else:
        nuevo_equipo = {'nombre_equipo': nombre, 'part_ganados': 0, 'part_empatados': 0, 'part_perdidos': 0, 'gol_favor': 0, 'gol_contra': 0}
        equipos.append(nuevo_equipo)
        return

def Cargar_Datos:
    """Carga los datos de puntos y goles"""
    for equipo in equipos:
        print("\nCarga de datos para el equipo " + equipo.nombre)
        equipo.part_ganados = input("Ingrese partidos ganados: ")
        equipo.part_empatados = input("Ingrese partidos empatados: ")
        equipo.part_perdidos = input("Ingrese partidos perdidos: ")
        equipo.gol_contra = input("Ingrese goles en contra: ")
        equipo.gol_favor = input("Ingrese goles a favor: ")

# Loop principal

equipos = []

cant_equipos = input("Ingrese cantidad de equipos: ")

for i in range(1,cant_equipos):
    Cargar_Equipos(equipos)


