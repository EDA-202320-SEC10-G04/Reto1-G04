﻿"""
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
 """

import config as cf
import model
import time
import csv
import csv

csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""



def new_controller(tipo_lista):
    """
    Crea una instancia del modelo
    """
    control = {
        "model" : None
    }
    control['model'] = model.new_data_structs(tipo_lista)
    return control



# Funciones para la carga de datos
    



def loadGoalscorers1(catalog, sample_option):
    """
    Carga los datos del archivo goalscorers.
    """
    


    goalscorersfile = cf.data_dir + f'football/goalscorers-utf8{sample_option}.csv'
    
    input_file = csv.DictReader(open(goalscorersfile, encoding='utf-8'))
    for goal in input_file:
        model.add_goalscorers1(catalog['model'], goal)

def loadResults1(catalog, sample_option):
    """
    Carga los datos del archivo results.
    """


    resultsfile = cf.data_dir + f'football/results-utf8{sample_option}.csv'
    input_file = csv.DictReader(open(resultsfile, encoding='utf-8'))
    for result in input_file:
        model.add_results1(catalog['model'], result)

def loadShootouts1(catalog, sample_option):
    """
    Carga los datos del archivo shootouts.
    """



    shootoutsfile = cf.data_dir + f'football/shootouts-utf8{sample_option}.csv'

    input_file = csv.DictReader(open(shootoutsfile, encoding='utf-8'))
    for shootout in input_file:
        model.add_shootouts1(catalog['model'], shootout)
# ...

def sortData(control, ordenamiento):
    """
    Ordena los datos y toma el tiempo de ordenamiento
    """

    start_time = get_time()
    model.sort(control["model"], ordenamiento)
    end_time = get_time()
    deltatime = delta_time(start_time, end_time)
    return deltatime


#limpiar listas
# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass

#re1
def sortName(data, name_team, condition_team, number_matchs):
    total_matchs = model.sortName(data, name_team, condition_team, number_matchs)
    return total_matchs

#req 2
def get_first_n_goals_by_player(control, player_name, n, recursive=True):
    "Retorna los goles totales de un jugador, y los últimos n goles"
    data_structs = control['model']
    start_time = get_time()
    total_goals, player_goals = model.get_first_n_goals_by_player(data_structs, player_name, n, recursive)
    end_time = get_time()
    
    deltatime = delta_time(start_time, end_time)
    return deltatime, total_goals, player_goals





def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass

#req 4
def queryMatchsbyPeriod(name_tournament, start_date, end_date, goalscore, results):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    matchs, total_coutries, total_cities,size = model.queryMatchsbyPeriod(name_tournament, start_date, end_date,goalscore, results)
    sizematches = model.lenght(matchs)
    sortmatchAlphabet = model.sortmatchAlphabet(matchs)
    
    Tmatchs = sixdata(sortmatchAlphabet)
    return Tmatchs, total_coutries, total_cities, size, sizematches




#Requerimiento 5

def consultar_anotaciones_jugador_periodo(control, jugador_nombre, fecha_inicio, fecha_fin, recursive = True):
    
    data_structs = control['model']
    total_goals, total_tournaments, penalties, own_goals, player_goals = model.consultar_anotaciones_jugador_periodo(data_structs, jugador_nombre, fecha_inicio, fecha_fin, recursive)
    return total_goals, total_tournaments, penalties, own_goals, player_goals

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed


def sixdata(tableList):
    if model.lt.size(tableList) <=6:
        return tableList
    else:
        firsts = getFirstNum(3, tableList)
        lasts = getLastNum(3, tableList)
        return model.listFusion(firsts, lasts)
def getFirstNum(number, tableList):
    return model.getFirstNum(number,tableList)

def getLastNum(number,tableList):
    return model.getLastNum(number,tableList)

def FindTeam(tableList, name):
    team = model.getnameTeam(tableList,name)
    
    return team
    
