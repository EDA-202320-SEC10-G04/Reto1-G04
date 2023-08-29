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
from datetime import datetime 
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

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
    #TODO: Inicializar las estructuras de datos
    pass


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    pass


# Funciones para creacion de datos

def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {
        "matches": lt.newList("ARRAY_LIST"),
        "goalscorers": lt.newList("ARRAY_LIST"),
        "shootouts": lt.newList("ARRAY_LIST")
    }
    return data_structs
def new_shootout_data(data):
    """
    Crea una nueva estructura para modelar los datos de una definición de partido desde el punto penal
    """
    shootout = {
        "date": data["date"],
        "home_team": data["home_team"],
        "away_team": data["away_team"],
        "winner": data["winner"]
    }
    return shootout
def new_goalscorer_data(data):
    """
    Crea una nueva estructura para modelar los datos de un goleador/anotación
    """
    goalscorer = {
        "date": data["date"],
        "home_team": data["home_team"],
        "away_team": data["away_team"],
        "scorer": data["scorer"],
        "minute": data["minute"],
        "penalty": data["penalty"],
        "own_goal": data["own_goal"]
    }
    return goalscorer

def new_match_data(data):
    """
    Crea una nueva estructura para modelar los datos de un partido
    """
    match = {
        "date": data["date"],
        "home_team": data["home_team"],
        "away_team": data["away_team"],
        "home_score": data["home_score"],
        "away_score": data["away_score"],
        "tournament": data["tournament"],
        "city": data["city"],
        "country": data["country"]
    }
    return match


def add_match_data(data_structs, data):
    """
    Agrega los datos de un partido a la estructura correspondiente
    """
    match = new_match_data(data)
    lt.addLast(data_structs["matches"], match)

def add_goalscorer_data(data_structs, data):
    """
    Agrega los datos de un jugador que marcó gol a la estructura correspondiente
    """
    goalscorer = new_goalscorer_data(data)
    lt.addLast(data_structs["goalscorers"], goalscorer)

def add_shootout_data(data_structs, data):
    """
    Agrega los datos de una definición de partido desde el punto penal a la estructura correspondiente
    """
    shootout = new_shootout_data(data)
    lt.addLast(data_structs["shootouts"], shootout)

# ...

def compare_matches(match1, match2):
    date1 = datetime.strptime(match1['date'], '%Y-%m-%d')
    date2 = datetime.strptime(match2['date'], '%Y-%m-%d')
        
    if date1 == date2:
        score_diff1 = int(match1['home_score']) - int(match1['away_score'])
        score_diff2 = int(match2['home_score']) - int(match2['away_score'])
            
        if score_diff1 == score_diff2:
            return 0
        else:
             return score_diff2 - score_diff1
    else:
        return date2 - date1

def sort_results(data_structs):
    all_matches = lt.newList("ARRAY_LIST")
    for match in lt.iterator(data_structs["matches"]):
        lt.addLast(all_matches, match)

    sorted_matches = sa.sort(all_matches, compare_matches)

    first_3_matches = lt.subList(sorted_matches, 1, 3)  # Corregir estos índices
    last_3_matches = lt.subList(sorted_matches, lt.size(sorted_matches) - 3, lt.size(sorted_matches))

    return first_3_matches + last_3_matches





def sort_goalscorers(data_structs):
    all_goalscorers = lt.newList("ARRAY_LIST")
    lt.addAll(all_goalscorers, data_structs["goalscorers"])
    
    def compare_goalscorers(goalscorer1, goalscorer2):
        date1 = datetime.strptime(goalscorer1['date'], '%Y-%m-%d')
        date2 = datetime.strptime(goalscorer2['date'], '%Y-%m-%d')
        
        if date1 == date2:
            minute_diff1 = int(goalscorer1['minute'])
            minute_diff2 = int(goalscorer2['minute'])
            
            if minute_diff1 == minute_diff2:
                return 0
            else:
                return minute_diff1 - minute_diff2
        else:
            return date2 - date1
    
    sorted_goalscorers = sa.sort(all_goalscorers, compare_goalscorers)
    
    first_3_goalscorers = lt.subList(sorted_goalscorers, 1, 3)
    last_3_goalscorers = lt.subList(sorted_goalscorers, lt.size(sorted_goalscorers) - 3, lt.size(sorted_goalscorers))
    
    return first_3_goalscorers + last_3_goalscorers


def sort_results(data_structs):
    all_matches = lt.newList("ARRAY_LIST")
    for match in lt.iterator(data_structs["matches"]):
        lt.addLast(all_matches, match)

    sorted_matches = sa.sort(all_matches, compare_matches)

    first_3_matches = lt.subList(sorted_matches, 1, 3)  # Corregir estos índices
    last_3_matches = lt.subList(sorted_matches, lt.size(sorted_matches) - 3, lt.size(sorted_matches))

    return first_3_matches + last_3_matches




def sort_shootouts(data_structs):
    all_shootouts = lt.newList("ARRAY_LIST")
    lt.addAll(all_shootouts, data_structs["shootouts"])
    
    def compare_shootouts(shootout1, shootout2):
        date1 = datetime.strptime(shootout1['date'], '%Y-%m-%d')
        date2 = datetime.strptime(shootout2['date'], '%Y-%m-%d')
        
        if date1 == date2:
            return shootout1['winner'] - shootout2['winner']
        else:
            return date2 - date1
    
    sorted_shootouts = sa.sort(all_shootouts, compare_shootouts)
    
    first_3_shootouts = lt.subList(sorted_shootouts, 1, 3)  # Corregir estos índices
    last_3_shootouts = lt.subList(sorted_shootouts, lt.size(sorted_shootouts) - 3, lt.size(sorted_shootouts))

    return first_3_shootouts + last_3_shootouts

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


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


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
