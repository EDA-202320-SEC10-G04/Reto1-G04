"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf
import datetime 
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos
# En model.py
def new_data_structs(tipo_lista):
    data = {
        'goalscore': None,
        'results': None,
        'shootouts': None,
    }
    if tipo_lista == "ARRAY_LIST":
        data['goalscore'] = lt.newList('ARRAY_LIST')
        data['results'] = lt.newList('ARRAY_LIST')
        data['shootouts'] = lt.newList('ARRAY_LIST')
    elif tipo_lista == "SINGLE_LINKED":
        data['goalscore'] = lt.newList('SINGLE_LINKED')
        data['results'] = lt.newList('SINGLE_LINKED')
        data['shootouts'] = lt.newList('SINGLE_LINKED')  
    return data
#limpiar las

        
def add_goalscorers1(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista de goleadores
    """
    lt.addLast(data_structs['goalscore'], data)

def add_results1(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista de resultados de partidos
    """
    lt.addLast(data_structs['results'], data)

def add_shootouts1(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista de definiciones de partidos desde el punto penal
    """
    lt.addLast(data_structs['shootouts'], data)


# ...

# Funciones de comparación
def compare_goalscore(data1, data2):
    # Ordenar primero por fecha
    date1 = datetime.datetime.strptime(data1['date'], '%Y-%m-%d')
    date2 = datetime.datetime.strptime(data2['date'], '%Y-%m-%d')

    if date1 < date2:
        return False
    elif date1 > date2:
        return True
    else:
        # Si las fechas son iguales, ordenar por minuto en que se anotó el gol

        minute1 = data1['minute']
        minute2 = data2['minute']
        
        # Comprobar si los minutos no son cadenas vacías antes de convertir a flotante
        if minute1 and minute2:
            if float(minute1) < float(minute2):
                return False
            elif float(minute1) > float(minute2):
                return True
            else:
                
                # Si el minuto es igual, comparar los nombres de los jugadores sin importar mayúsculas y minúsculas
                player1 = data1['scorer'].lower()
                player2 = data2['scorer'].lower()
                if player1 > player2:
                    return True
                elif player1 < player2 :
                    return False
                else:
                    return False
 


def compare_results(data1, data2):
    # Ordenar primero por fecha, luego por puntaje local y puntaje visitante
    date1 = datetime.datetime.strptime(data1['date'], '%Y-%m-%d')
    date2 = datetime.datetime.strptime(data2['date'], '%Y-%m-%d')
    
    if date1 < date2:
        return False
    elif date1 > date2:
        return True
    else:
        if float(data1['home_score']) < float((data2['home_score'])):
            return False
        elif float(data1['home_score']) > float(data2['home_score']):
            return True
        else:
            if float(data1['away_score']) < float(data2['away_score']):
                return False
            elif float(data1['away_score']) > float(data2['away_score']):
                return True
            else:
                return False

def compare_shootouts(data1, data2):
    # Ordenar primero por fecha
    date1 = datetime.datetime.strptime(data1['date'], '%Y-%m-%d')
    date2 = datetime.datetime.strptime(data2['date'], '%Y-%m-%d')
    
    if date1 < date2:
        return False
    elif date1 > date2:
        return True
    else:
        # Si las fechas son iguales, comparar los nombres de los equipos sin importar mayúsculas y minúsculas
        team1 = data1['home_team'].lower()
        team2 = data2['home_team'].lower()
        if team1 < team2:
            return False
        elif team1 > team2:
            return True
        else:
            ateam1 = data1['away_team'].lower()
            ateam2 = data2['away_team'].lower()
            return False if ateam1 < ateam2 else True if ateam1 > ateam2 else False
        # En model.py
def cmp_partidos_by_fecha_y_pais(resultado1, resultado2):
    """
    Devuelve verdadero (True) si la fecha del resultado1 es menor que en el resultado2,
    en caso de que sean iguales tenga el nombre de la ciudad en que se disputó el partido,
    de lo contrario devuelve falso (False).
    Args:
    resultado1: información del primer registro de resultados FIFA que incluye
    “date” y el “country”
    resultado2: información del segundo registro de resultados FIFA que incluye
    “date” y el “country”
    """
    date_format = "%Y-%m-%d"
    date1 = datetime.datetime.strptime(resultado1['date'], date_format)
    date2 = datetime.datetime.strptime(resultado2['date'], date_format)

    if date1 != date2:
        return date1 < date2
    else:
        # Si las fechas son iguales, ordenar por nombre de país
        country1 = resultado1['home_team']
        country2 = resultado2['home_team']
        return country1 < country2
        

def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass

#req 2
def get_first_n_goals_by_player(catalog, player_name, n,  recursive=True):
    if recursive:
        return recurs_get_first_n_goals_by_player(catalog, player_name, n)
    else:
        return  iter_get_first_n_goals_by_player(catalog, player_name, n)
#Iterativa
def iter_get_first_n_goals_by_player(data_structs, player_name, n):
    player_goals = lt.newList('ARRAY_LIST')
    total_goals = 0
    sa.sort(data_structs["goalscore"], cmp_partidos_by_fecha_y_pais)
    # Recorremos la lista de goles y seleccionamos los que coincidan con el jugador
    for goal in lt.iterator(data_structs['goalscore']):
        if goal['scorer'].lower() == player_name.lower():
            lt.addLast(player_goals, goal)
            total_goals += 1
            if total_goals == n:
                break
    return total_goals, player_goals
#Recursiva
def recurs_get_first_n_goals_by_player(data_structs, player_name, n):
    def recursive_goals(goals, player_goals, total_goals, index):
        if index >= lt.size(goals) or total_goals >= n:
            return total_goals, player_goals
        
        goal = lt.getElement(goals, index)
        if goal['scorer'].lower() == player_name.lower():
            lt.addLast(player_goals, goal)
            total_goals += 1
        
        return recursive_goals(goals, player_goals, total_goals, index + 1)

    player_goals = lt.newList('ARRAY_LIST')
    total_goals = 0
    sa.sort(data_structs["goalscore"], cmp_partidos_by_fecha_y_pais)
    goals = data_structs['goalscore']
    
    return recursive_goals(goals, player_goals, total_goals, 0)


def get_total_goals_by_player(data_structs, player_name):
    
    goals = data_structs['goalscore']
    player_goals = lt.newList('ARRAY_LIST')
    
    for goal in lt.iterator(goals):
        if goal['scorer'].lower() == player_name.lower():
            lt.addLast(player_goals, goal)
    se.sort(player_goals, cmp_partidos_by_fecha_y_pais)
    return lt.size(player_goals)

def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass




    
# Funciones de ordenamiento

def sort(data, ordenamiento):
    # Ordenar las listas usando los criterios de comparación definidos
    if ordenamiento == "Shell".lower():
        #sa.sort(data['goalscore'], cmp_partidos_by_fecha_y_pais)
        sa.sort(data['results'], cmp_partidos_by_fecha_y_pais)
        #sa.sort(data['shootouts'], cmp_partidos_by_fecha_y_pais)
    elif ordenamiento == "Selection".lower():
        #se.sort(data['goalscore'], cmp_partidos_by_fecha_y_pais)
        se.sort(data['results'], cmp_partidos_by_fecha_y_pais)
        #se.sort(data['shootouts'], cmp_partidos_by_fecha_y_pais)    
    elif ordenamiento == "Insertion".lower():
        #ins.sort(data['goalscore'], cmp_partidos_by_fecha_y_pais)
        ins.sort(data['results'], cmp_partidos_by_fecha_y_pais)
        #ins.sort(data['shootouts'], cmp_partidos_by_fecha_y_pais)    
       

# Funciones de ordenamiento



def getFirstNum(number, tablelist):
    if number <= lt.size(tablelist):
        firsts = lt.newList('ARRAY_LIST')
        for element in range(1, number+1):
            d = lt.getElement(tablelist, element)
            lt.addLast(firsts, d)
        return firsts
    else:
        return tablelist
def getLastNum(number, tablelist):
    if number <= lt.size(tablelist):
        last = lt.newList('ARRAY_LIST')
        for element in range(0,number):
            d = lt.getElement(tablelist, lt.size(tablelist)-element)
            lt.addFirst(last, d)
        return last
    else:
        return tablelist

def listFusion(list1, list2):
    listfusion = lt.newList('ARRAY_LIST')
    for element in lt.iterator(list1):
        lt.addLast(listfusion, element)
    for element in lt.iterator(list2):
        lt.addLast(listfusion, element)
    return listfusion