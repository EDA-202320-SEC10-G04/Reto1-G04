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

def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data = {
        'goalscore': None,
        'results': None,
        'shootouts': None,
    }

    data['goalscore'] = lt.newList('ARRAY_LIST', cmpfunction=compare_goalscore)
    data['results'] = lt.newList('ARRAY_LIST', cmpfunction=compare_results)
    data['shootouts'] = lt.newList('ARRAY_LIST', cmpfunction=compare_shootouts)
    return data

def add_goalscorers(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista de goleadores
    """
    lt.addLast(data_structs['goalscore'], data)

def add_results(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista de resultados de partidos
    """
    lt.addLast(data_structs['results'], data)

def add_shootouts(data_structs, data):
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
        return -1
    elif date1 > date2:
        return 1
    else:
        # Si las fechas son iguales, ordenar por minuto en que se anotó el gol
        if data1['minute'] < data2['minute']:
            return -1
        elif data1['minute'] > data2['minute']:
            return 1
        else:
            
            # Si el minuto es igual, comparar los nombres de los jugadores sin importar mayúsculas y minúsculas
            player1 = data1['scorer'].lower()
            player2 = data2['scorer'].lower()
            return -1 if player1 < player2 else 1 if player1 > player2 else 0

def compare_results(data1, data2):
    # Ordenar primero por fecha, luego por puntaje local y puntaje visitante
    date1 = datetime.datetime.strptime(data1['date'], '%Y-%m-%d')
    date2 = datetime.datetime.strptime(data2['date'], '%Y-%m-%d')
    
    if date1 < date2:
        return -1
    elif date1 > date2:
        return 1
    else:
        if data1['home_score'] < data2['home_score']:
            return -1
        elif data1['home_score'] > data2['home_score']:
            return 1
        else:
            if data1['away_score'] < data2['away_score']:
                return -1
            elif data1['away_score'] > data2['away_score']:
                return 1
            else:
                return 0

def compare_shootouts(data1, data2):
    # Ordenar primero por fecha
    date1 = datetime.datetime.strptime(data1['date'], '%Y-%m-%d')
    date2 = datetime.datetime.strptime(data2['date'], '%Y-%m-%d')
    
    if date1 < date2:
        return -1
    elif date1 > date2:
        return 1
    else:
        # Si las fechas son iguales, comparar los nombres de los equipos sin importar mayúsculas y minúsculas
        team1 = data1['home_team'].lower()
        team2 = data2['home_team'].lower()
        if team1 < team2:
            return -1
        elif team1 > team2:
            return 1
        else:
            team1 = data1['away_team'].lower()
            team2 = data2['away_team'].lower()
            return -1 if team1 < team2 else 1 if team1 > team2 else 0
# ...
def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


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
def sort(data):
    # Ordenar las listas usando los criterios de comparación definidos
    quk.sort(data['goalscore'], compare_goalscore)
    quk.sort(data['results'], compare_results)
    quk.sort(data['shootouts'], compare_shootouts)

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