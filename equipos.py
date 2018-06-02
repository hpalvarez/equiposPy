# Programa que carga equipos y puntajes y arma tabla de posiciones

def Cargar_Equipos():
    """Carga los nombres e inicializa los equipos"""
    nombre = input("Ingrese el nombre del equipo: ")
    nuevo_equipo = {'nombre_equipo': nombre, 'part_ganados': 0, 'part_empatados': 0, 'part_perdidos': 0, 'gol_favor': 0, 'gol_contra': 0}
    return nuevo_equipo

def Cargar_Datos(equipos):
    """Carga los datos de puntos y goles"""
    for equipo in equipos:
        print("\nCarga de datos para el equipo " + equipo.nombre_equipo)
        equipo.part_ganados = input("Ingrese partidos ganados: ")
        equipo.part_empatados = input("Ingrese partidos empatados: ")
        equipo.part_perdidos = input("Ingrese partidos perdidos: ")
        equipo.gol_contra = input("Ingrese goles en contra: ")
        equipo.gol_favor = input("Ingrese goles a favor: ")

# Función principal 

#Inicializo la lista de equipos

equipos = []

# Pregunto cantidad

cant_equipos = input("Ingrese cantidad de equipos: ")

# Cargo los equipos

for i in range(0,int(cant_equipos)):
    nuevo_equipo = Cargar_Equipos()
    equipos.append(nuevo_equipo)

# Cargo los datos

Cargar_Datos(equipos)