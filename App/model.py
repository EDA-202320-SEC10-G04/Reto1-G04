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
    data = {
        'goalscore': None,
        'results': None,
        'shootouts': None,
    }
    data['goalscore'] = lt.newList('ARRAY_LIST')
    data['results'] = lt.newList('ARRAY_LIST')
    data['shootouts'] = lt.newList('ARRAY_LIST')
    data['unique_goalscorers'] = set()  # Conjunto para evitar duplicados en goleadores
    data['unique_results'] = set()      # Conjunto para evitar duplicados en resultados
    data['unique_shootouts'] = set()    # Conjunto para evitar duplicados en shootouts
    return data

def add_goalscorers(data_structs, data):
    if data['scorer'] not in data_structs['unique_goalscorers']:
        lt.addLast(data_structs['goalscore'], data)
        data_structs['unique_goalscorers'].add(data['scorer'])

def add_results(data_structs, data):
    if (data['home_team'], data['away_team']) not in data_structs['unique_results']:
        lt.addLast(data_structs['results'], data)
        data_structs['unique_results'].add((data['home_team'], data['away_team']))

def add_shootouts(data_structs, data):
    if (data['home_team'], data['away_team']) not in data_structs['unique_shootouts']:
        lt.addLast(data_structs['shootouts'], data)
        data_structs['unique_shootouts'].add((data['home_team'], data['away_team']))

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
    sa.sort(data['goalscore'], compare_goalscore)
    sa.sort(data['results'], compare_results)
    sa.sort(data['shootouts'], compare_shootouts)

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