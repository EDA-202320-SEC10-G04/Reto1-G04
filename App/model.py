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
def cmp_date_and_minute(data1, data2):
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
            else:
                return True

 


def cmp_fecha_país_mayor_menor(data1, data2):
    # Ordenar primero por fecha, luego por puntaje local y puntaje visitante
    date1 = datetime.datetime.strptime(data1['date'], '%Y-%m-%d')
    date2 = datetime.datetime.strptime(data2['date'], '%Y-%m-%d')
    
    if date1 < date2:
        return False
    elif date1 > date2:
        return True
    else:
        if (data1['home_team']) < ((data2['home_team'])):
            return False
        elif (data1['home_team']) > (data2['home_team']):
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
        

       
def compare_home(data1, data2):
    team1 = data1['home_team'].lower()
    team2 = data2['home_team'].lower()
    if team1 < team2:
        return True
    elif team1 > team2:
        return False
def compare_away(data1, data2):
    team1 = data1['away_team'].lower()
    team2 = data2['away_team'].lower()
    if team1 < team2:
        return True
    elif team1 > team2:
        return False

def compare_country(data1, data2):
    team1 = data1['country'].lower()
    team2 = data2['country'].lower()
    if team1 < team2:
        return True
    elif team1 > team2:
        return False
#req1
def compare_countryMoretoLess(data1, data2):
    team1 = data1['country'].lower()
    team2 = data2['country'].lower()
    if team1 > team2:
        return True
    elif team1 < team2:
        return False

def sortName(data,name_team, condition_team, number_matchs):
    e =0
    total_indices = []
    if condition_team.lower() == "local":
        f ="home_team"
        indices, NameSort= searchname(data,name_team, condition_team, number_matchs,f)
        total_indices = indices
    
    elif condition_team.lower() == "visitante":
        f ="away_team"
        indices, NameSort= searchname(data,name_team, condition_team, number_matchs,f)
        total_indices = indices


    else:
        e =1
        f ="home_team"
        indices1, NameSort1= searchname(data,name_team, condition_team, number_matchs,f)
        z ="away_team"
        indices2, NameSort2= searchname(data,name_team, condition_team, number_matchs,z)      
    if e==1:
        total_teams = lt.newList('ARRAY_LIST')
        answerSort = lt.newList('ARRAY_LIST')
        for i in indices1:
            element= lt.getElement(NameSort1,i+1)
            lt.addFirst(total_teams,element)
        for i in indices2:
            element= lt.getElement(NameSort2,i+1)
            lt.addFirst(total_teams,element)
        answer= sa.sort(total_teams, compare_shootouts)
        answerSort = getFirstNum(number_matchs,answer)
        return answerSort

    else:
        total_teams = lt.newList('ARRAY_LIST')
        answerSort = lt.newList('ARRAY_LIST')
        for i in total_indices:
            element= lt.getElement(NameSort,i+1)
            lt.addFirst(total_teams,element)
        answer= sa.sort(total_teams, compare_shootouts)
        answerSort = getFirstNum(number_matchs,answer)
        return answerSort
 

def searchname(data,name_team,  f):
        NameSort = lt.newList('ARRAY_LIST')
        newList = []
        if f=='home_team':
            NameSort = sa.sort(data, compare_home)
        else:
            NameSort = sa.sort(data, compare_away)
        for name in lt.iterator(NameSort):
            
            name_value = name[f].lower()
            newList.append(name_value)
        
        i = 0
        work = True
        indices = []
        izquierda = 0
        derecha = len(newList) - 1
        x = newList
        while izquierda <= derecha and work:
            medio = (izquierda + derecha) // 2  # Encontramos el índice medio de la lista
            r = newList[medio]
            z = name_team.lower()
            if newList[medio] == name_team.lower():
                indices.append(medio)  # Hemos encontrado el elemento y agregamos su índice a la lista
                # Buscamos más ocurrencias hacia la izquierda
                i = medio - 1
                while i >= 0 and newList[i] == name_team.lower():
                    indices.append(i)
                    i -= 1
                # Buscamos más ocurrencias hacia la derecha
                j = medio + 1
                while j < len(newList) and newList[j] == name_team.lower():
                    indices.append(j)
                    j += 1
                work = False

            elif newList[medio] < name_team.lower():
                izquierda = medio + 1  # El elemento está en la mitad derecha
            else:
                derecha = medio - 1  # El elemento está en la mitad izquierda
        return indices, NameSort

#req 2
def get_first_n_goals_by_player(catalog, player_name, n,  recursive=True):
    if recursive:
        return recurs_get_first_n_goals_by_player(catalog, player_name, n)
    else:
        return iter_get_first_n_goals_by_player(catalog, player_name, n)
#Iterativa
def iter_get_first_n_goals_by_player(data_structs, player_name, n):
    player_goals = lt.newList('ARRAY_LIST')
    total_goals = 0
    sa.sort(data_structs["goalscore"], cmp_fecha_país_mayor_menor)
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
    sa.sort(data_structs["goalscore"], cmp_fecha_país_mayor_menor )
    goals = data_structs['goalscore']

    return recursive_goals(goals, player_goals, total_goals, 0)

#Req 3
def req_3(data_structs):
    pass
#Req 5
def queryMatchsbyPeriod(name_tournament, start_date, end_date,shootouts, results):
    """
    Función que soluciona el requerimiento 4
    """
    newarray = lt.newList('ARRAY_LIST')
    goals =sa.sort(shootouts,compare_home)
    total_paises = set()
    total_ciudades = set()
    sa.sort(shootouts,compare_away)
    start_date= datetime.datetime.strptime(start_date,"%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date,"%Y-%m-%d")
    r = lt.newList('ARRAY_LIST')
    for i in lt.iterator(results):
        date = datetime.datetime.strptime(i['date'],"%Y-%m-%d")
        if date<= end_date and date>= start_date and i['tournament']== name_tournament:
            country = i['country']
            city = i['city']
            total_paises.add(country)
            total_ciudades.add(city)
            if i['home_score'] == i['away_score']:
                winner = buscar_ganador(shootouts, date, i['home_team'], i ['away_team'])
            else:
                winner = 'Unknown'
            i['winner'] = winner
            lt.addLast(newarray, i)




        
        


    size = lt.size(newarray)
    return newarray, len(total_paises), len(total_ciudades),size
def buscar_ganador(shootouts,date, home_team, away_team):
    winner = 'Unkown'
    for i in lt.iterator(shootouts):
        datei = datetime.datetime.strptime(i['date'],"%Y-%m-%d")
        if date == datei and i['home_team'] == home_team and i['away_team'] == away_team:
            return i['winner']



def sortmatchAlphabet(data):
   
    sa.sort(data, cmp_fecha_país_mayor_menor)
    return data

def lenght(data):
    return lt.size(data)

#search name binary
def searchnameBinary(data, goal, key, goal2, key2):
    low, high = 0 , lt.size(data)
    x =-1
    while low<= high:
        mid = (low + high) // 2
        f=lt.getElement(data,mid)[key].lower()
        if lt.getElement(data,mid)[key].lower()  ==goal.lower() :
            if lt.getElement(data,mid)[key2].lower() == goal2.lower():
                x = mid
                return x
            else:
                work =True
                while work:
                     #buscamos en la izquierda mas ocurrencias
                    if lt.getElement(data,mid)[key].lower()  ==goal.lower():
                        mid-=1
                    else:
                        work = False
                        x = mid+1
                    #buscamos mas iteraciones a la izquierda
                working = True
                while working:
                    if lt.getElement(data,x)[key].lower()  ==goal.lower():
                        if lt.getElement(data,x)[key2].lower() == goal2.lower():
                            return x
                    if lt.getElement(data,x)[key].lower()  ==goal.lower():
                            x+=1
                    else:
                        working = False

        elif lt.getElement(data,mid)[key].lower() <goal.lower():
            
            low = mid+1
            
        else:
            high= mid-1

    return  x




#Req 5
def consultar_anotaciones_jugador_periodo(data_structs, jugador_nombre, fecha_inicio, fecha_fin, recursive = True):
    if recursive:
        return rec_consultar_anotaciones_jugador_periodo(data_structs, jugador_nombre, fecha_inicio, fecha_fin)
    else:
        return iter_consultar_anotaciones_jugador_periodo(data_structs, jugador_nombre, fecha_inicio, fecha_fin)
    
#Iterativa
def iter_consultar_anotaciones_jugador_periodo(data_structs, jugador_nombre, fecha_inicio, fecha_fin):
    """
    Consulta las anotaciones de un jugador en un período de tiempo.
    Devuelve una lista de goles del jugador en ese período.
    """
    player_goals = lt.newList('ARRAY_LIST')

    # Ordena la lista de goles por fecha y minuto
    sa.sort(data_structs['goalscore'], cmp_date_and_minute)

    total_goals = 0
    total_tournaments = set()
    penalties = 0
    own_goals = 0
    fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
    fecha_fin = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d')
    for goal in lt.iterator(data_structs['goalscore']):
        goal_date = datetime.datetime.strptime(goal['date'], '%Y-%m-%d')
        if fecha_inicio <= goal_date <= fecha_fin and goal['scorer'].lower() == jugador_nombre.lower():
            total_goals += 1
            # Obtener el nombre del torneo desde la lista de resultados
            tournament = buscar_torneo(data_structs['results'], goal['date'], goal['home_team'], goal['away_team'])
            if tournament:
                total_tournaments.add(tournament)
            if goal['penalty'] == 'True':
                penalties += 1
            if goal['own_goal'] == 'True':
                own_goals += 1

            # Incluir el nombre del torneo en el gol
            goal['tournament'] = tournament
            lt.addLast(player_goals, goal)

    return total_goals, len(total_tournaments), penalties, own_goals, player_goals


#Recursiva 
def rec_consultar_anotaciones_jugador_periodo(data_structs, jugador_nombre, fecha_inicio, fecha_fin):
    def recursive_goals(goals, player_goals, total_goals, total_tournaments, penalties, own_goals, index):
        if index >= lt.size(goals):
            return total_goals, len(total_tournaments), penalties, own_goals, player_goals
        
        goal = lt.getElement(goals, index)
        goal_date = datetime.datetime.strptime(goal['date'], '%Y-%m-%d')

        if fecha_inicio <= goal_date <= fecha_fin and goal['scorer'].lower() == jugador_nombre.lower():
            total_goals += 1
            # Obtener el nombre del torneo desde la lista de resultados
            tournament = buscar_torneo(data_structs['results'], goal['date'], goal['home_team'], goal['away_team'])
            if tournament:
                total_tournaments.add(tournament)
            if goal['penalty'] == 'True':
                penalties += 1
            if goal['own_goal'] == 'True':
                own_goals += 1

            # Incluir el nombre del torneo en el gol
            goal['tournament'] = tournament
            lt.addLast(player_goals, goal)
        
        return recursive_goals(goals, player_goals, total_goals, total_tournaments, penalties, own_goals, index + 1)

    player_goals = lt.newList('ARRAY_LIST')
    total_goals = 0
    total_tournaments = set()
    penalties = 0
    own_goals = 0
    fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
    fecha_fin = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d')
    sa.sort(data_structs["goalscore"], cmp_date_and_minute)
    goals = data_structs['goalscore']

    return recursive_goals(goals, player_goals, total_goals, total_tournaments, penalties, own_goals, 0)
def buscar_torneo(results, goal_date, home_team, away_team):
    """
    Busca el nombre del torneo en la lista de resultados según la fecha y los equipos.
    """
    for result in lt.iterator(results):
        result_date = datetime.datetime.strptime(result['date'], '%Y-%m-%d')
        if result_date == datetime.datetime.strptime(goal_date, '%Y-%m-%d') and result['home_team'] == home_team and result['away_team'] == away_team:
            return result['tournament']
    return 'Desconocido'
#Req 6
"""
def Clasifica_mejores_equipos_de_un_torneo(data_structs, nombre_torneo, fecha_inicio, fecha_fin):
    player_goals = lt.newList('ARRAY_LIST')

    # Ordena la lista de goles por fecha y minuto
    sa.sort(data_structs['goalscore'], cmp_date_and_minute)

    total_matches = 0
    total_equipos = set()
    penalties = 0
    own_goals = 0
    fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d')
    fecha_fin = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d')
    for goal in lt.iterator(data_structs['goalscore']):
        goal_date = datetime.datetime.strptime(goal['results'], '%Y-%m-%d')
        if fecha_inicio <= goal_date <= fecha_fin and goal['tournament'].lower() == nombre_torneo.lower():
            total_matches += 1
            # Obtener el nombre del torneo desde la lista de resultados
            tournament = buscar_torneo(data_structs['results'], goal['date'], goal['home_team'], goal['away_team'])
            if tournament:
                total_tournaments.add(tournament)
            if goal['penalty'] == 'True':
                penalties += 1
            if goal['own_goal'] == 'True':
                own_goals += 1

            # Incluir el nombre del torneo en el gol
            goal['tournament'] = tournament
            lt.addLast(player_goals, goal)

    return total_goals, len(total_tournaments), penalties, own_goals, player_goals
"""

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

def getnameTeam(tableList,name):
    nameTeam = lt.newList('ARRAY_LIST')
    x =lt.compareElements(tableList, name, element)
    for element in lt.iterator(tableList['home_team']):
        if name == element:
            nameTeam.addLast(element)


