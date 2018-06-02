# Programa que carga equipos y puntajes y arma tabla de posiciones

from operator import itemgetter

def Cargar_Equipos(equipos):
    """Carga los nombres e inicializa los equipos"""
    nombre = input("Ingrese el nombre del equipo: ")
    nuevo_equipo = {'nombre_equipo': nombre, 'part_ganados': 0, 'part_empatados': 0, 'part_perdidos': 0, 'gol_favor': 0, 'gol_contra': 0, 'puntos': 0, 'dif_gol': 0, 'part_jugados': 0}
    equipos.append(nuevo_equipo)

def Cargar_Datos(equipos):
    """Carga los datos de puntos y goles"""
    for indice in range(0,len(equipos)):
        print("\nCarga de datos para el equipo " + equipos[indice]['nombre_equipo'])
        equipos[indice]['part_ganados'] = int(input("Ingrese partidos ganados: "))
        equipos[indice]['part_empatados'] = int(input("Ingrese partidos empatados: "))
        equipos[indice]['part_perdidos'] = int(input("Ingrese partidos perdidos: "))
        equipos[indice]['gol_favor'] = int(input("Ingrese partidos goles a favor: "))
        equipos[indice]['gol_contra'] = int(input("Ingrese partidos goles en contra: "))
        equipos[indice]['puntos'] = (equipos[indice]['part_ganados'] * 3) + equipos[indice]['part_empatados']
        equipos[indice]['dif_gol'] = equipos[indice]['gol_favor'] - equipos[indice]['gol_contra']
        equipos[indice]['part_jugados'] = equipos[indice]['part_ganados'] + equipos[indice]['part_empatados'] + equipos[indice]['part_perdidos']

def Imprimir_Encabezado():
    """Imprime el encabezado de la tabla de posiciones"""
    print("\nEquipo                PTS  PJ  PG  PE  PP  GF  GC  DIF\n")
    print("------------------------------------------------------\n")

def Imprimir_Contenido(equipos_ordenados):
    for indice in range(0,len(equipos_ordenados)):
        print('{0: <22}'.format(equipos_ordenados[indice]['nombre_equipo']), end='')
        print('{0: <4}'.format(equipos_ordenados[indice]['puntos']), end='')
        print('{0: <4}'.format(equipos_ordenados[indice]['part_jugados']), end='')
        print('{0: <4}'.format(equipos_ordenados[indice]['part_ganados']), end='')
        print('{0: <4}'.format(equipos_ordenados[indice]['part_empatados']), end='')
        print('{0: <4}'.format(equipos_ordenados[indice]['part_perdidos']), end='')
        print('{0: <4}'.format(equipos_ordenados[indice]['gol_favor']), end='')
        print('{0: <4}'.format(equipos_ordenados[indice]['gol_contra']), end='')
        print('{0: <4}'.format(equipos_ordenados[indice]['dif_gol']))

# Función principal 

#Inicializo la lista de equipos

equipos = []

# Pregunto cantidad

cant_equipos = input("Ingrese cantidad de equipos: ")

# Cargo los equipos

for i in range(0,int(cant_equipos)):
    Cargar_Equipos(equipos)

# Cargo los datos

Cargar_Datos(equipos)

# Imprimo el encabezado de la tabla

Imprimir_Encabezado()

# Imprimo el contenido

equipos_ordenados = sorted(equipos, key = itemgetter('puntos'), reverse = True)
Imprimir_Contenido(equipos_ordenados)