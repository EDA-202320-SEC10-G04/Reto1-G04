"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
from tabulate import tabulate
import traceback
from prettytable import PrettyTable, ALL


default_limit = 1000
sys.setrecursionlimit(default_limit*100)
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Listar los partidos de un equipo")
    print("3- Listar los primeros goles anotados por un jugador")
    print("4- Consultar los partidos que disputo un equipo en un periodo de tiempo")
    print("5- Consultar los partidos en un torneo durante un periodo de tiempo")
    print("6- Consultar anotaciones de un jugador en un periodo de tiempo")
    print("7- Clasificar los mejores equipos de un torneo en un periodo")
    print("8- Clasificar los mejores anotadores en partidos oficiales en un periodo")
    print("9- Comparar el desempeño de dos selecciones en torneos oficiales")
    print("0- Salir")
#pretty table
def printSimpleTable(tableList, keys):
    table = PrettyTable()
    table.max_width = 20
    table.hrules =ALL
    table.field_names = keys
    lines = []
    for element in lt.iterator(tableList):
        line = []
        for key in keys:
            stringE = str(element[key])
            if len(stringE) > 20:
                stringE = stringE[:20]
            line.append(stringE)
        lines.append(line)
    table.add_rows(lines)
    print(table)
def load_data_s_r(control):
    """
    Carga los datos desde los archivos CSV.
    """

    goal_score_count = controller.loadGoalscorers1(control)
    result_count = controller.loadResults1(control)
    shootout_count = controller.loadShootouts1(control)
    controller.loadData(control)
    return goal_score_count, result_count, shootout_count


    
def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass

def print_first_n_goals_by_player(total_goals, player_goals):
    print(f"Total de goles anotados por el jugador: {total_goals}\n")
    print("Detalles de los goles:")
    
    if total_goals > 0:
        keys = ['date', 'home_team', 'away_team', 'scorer', 'minute', 'penalty', 'own_goal']

        printSimpleTable(player_goals, keys)

        if total_goals > 6:
            player_goals = controller.sixdata(player_goals)
            printSimpleTable(player_goals, keys)
    else:
        print("No se encontraron goles para el jugador especificado.")



def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
    
            load_data_s_r(control)
            print('Match result count: ' + str(lt.size(control['model']['results'])))
            print('Goal scorers count: ' + str(lt.size(control['model']['goalscore'])))
            print('shootout-penalty definition count: ' + str(lt.size(control['model']['shootouts'])))
            #--------------------MATCH RESULTS ----------------------
            print("--------------------MATCH RESULTS --------------------")
            sixResults =controller.sixdata(control['model']['results'])
            printSimpleTable(sixResults, ['date','home_team','away_team','home_score','away_score','country','city','tournament'])
           # -----------GOAL SCORES-----------------------------
            print("-------------------GOAL SCORES-----------------------------")
            sixgoals = controller.sixdata(control['model']['goalscore'])
            printSimpleTable(sixgoals,['date','home_team','away_team','scorer','team','minute','penalty','own_goal'])
            # ------------------- SHOOTOUS----------------------------------------------------------------
            print("----------------------SHOOTOUS----------------------------------------------------------------")
            sixshoots = controller.sixdata(control['model']['shootouts'])
            printSimpleTable(sixshoots,['date','home_team','away_team','winner'])


        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            player_name = input("Ingrese el nombre del jugador: ")
            n = int(input("Ingrese el número de goles a mostrar: "))
            total_goals, player_goals = controller.get_first_n_goals_by_player(control, player_name, n)
            print_first_n_goals_by_player(total_goals, player_goals)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)

