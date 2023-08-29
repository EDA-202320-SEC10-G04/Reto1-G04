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


def new_controller():
    """
    Crea una instancia del modelo
    """
    # Llamar la función del modelo que crea las estructuras de datos
    data_structs = model.new_data_structs()
    control = {
        'data_structs': data_structs
    }
    return control


# Funciones para la carga de datos

def load_data(control, filename, data_type):
    """
    Carga los datos desde un archivo CSV en el modelo
    """
    data_structs = control['data_structs']
    full_path = f"Data/football/{filename.replace('utf8', 'utf8-small')}"  # Ruta completa
    
    with open(full_path, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if data_type == "results":
                model.add_match_data(data_structs, row)
            elif data_type == "goalscorers":
                model.add_goalscorer_data(data_structs, row)
            elif data_type == "shootouts":
                model.add_shootout_data(data_structs, row)
    
    print(f"Datos cargados desde {full_path}")



# Función para obtener las estructuras de datos
def get_data_structs(control):
    """
    Obtiene las estructuras de datos del modelo
    """
    return control["data_structs"]



# Funciones de ordenamiento
def sort_results(control):
    """
    Retorna el resultado del requerimiento 1
    """
    matches = model.sort_results(control["data_structs"])
    return matches
def sort_goalscorers(control):
    return model.sort_goalscorers(control["data_structs"])

def sort_shootouts(control):
    return model.sort_shootouts(control["data_structs"])

# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

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
