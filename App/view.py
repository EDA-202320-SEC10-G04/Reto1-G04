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
import traceback
from prettytable import PrettyTable, ALL
import threading


default_limit = 1000
sys.setrecursionlimit(default_limit*100)
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller(tipo_lista="ARRAY_LIST"):
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control = controller.new_controller(tipo_lista)
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
    print("9- Seleccionar el tipo de lista y el tipo de ordenamiento")
    print("10- Cambiar tipo de algoritmos (recursivos o iterativos)")
    print("0- Salir")
#pretty table
def printSimpleTable(tableList, keys):
    """
    Función encargada de mostrar los datos en tablas
    """
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
def load_data_s_r(control, sample_option):
    """
    Carga los datos desde las funciones de carga de datos y devuelve las listas.
    """

    goal_score_count = controller.loadGoalscorers1(control, sample_option)
    result_count = controller.loadResults1(control, sample_option)
    shootout_count = controller.loadShootouts1(control, sample_option)
    
    return goal_score_count, result_count, shootout_count
def sortData(control, ordenamiento):
    time = controller.sortData(control, ordenamiento)
    return time
    
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
    """Muestra los goles del jugador usando printSimpleTable

    Args:
        total_goals (int): Total de goles
        player_goals (int): Total de goles por jugador
    """
    print(f"Total de goles anotados por el jugador: {total_goals}\n")
    print("Detalles de los goles:")
    
    if total_goals > 0:
        keys = ['date', 'home_team', 'away_team', 'scorer', 'minute', 'penalty', 'own_goal']

        

        if total_goals > 6:
            player_goals = controller.sixdata(player_goals)
         
        printSimpleTable(player_goals,keys)
         
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

bool_lt_opt = ("s", "S", "1", True, "true", "True", "si", "Si", "SI")

def menu_cycle():

    """
    Menu principal
    """
    working = True
    # configurando si usa algoritmos recursivos
    rec = True
    #ciclo del menu
    control = new_controller()
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
                        
            tipo_lista = "ARRAY_LIST"
            sample_option = input("Selecciona el tamaño de muestra (-5pct, -20pct, -30pct, -50pct, -large): ")
            load_data_s_r(control, sample_option)
 

            print(f"Tamaño de muestra seleccionado: {len(sample_option)}")
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
            number_matchs =int( input("Ingrese el numero de partidos: "))
            name_team = input("Ingrese el nombre del Equipo: ")
            condition_team = input("Ingrese la condicion del equipo (local, visitante o indiferente): ")
            total_matchs = controller.sortName(control['model']['results'], name_team, condition_team, number_matchs)
            printSimpleTable(total_matchs,['date','home_team','away_team','country','city','home_score','away_score'])

        elif int(inputs) == 3:
            player_name = input("Ingrese el nombre del jugador: ")
            n = int(input("Ingrese el número de goles a mostrar: "))
            total_goals, player_goals = controller.get_first_n_goals_by_player(control, player_name, n, recursive=rec)
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
            tipo_lista = input("Qué tipo de lista deseas [ARRAY_LIST] o [SINGLE_LINKED]: ")
            if tipo_lista.upper() == "ARRAY_LIST" or tipo_lista.upper() == "SINGLE_LINKED":
             control = new_controller(tipo_lista)
             print(f"Los datos se han cargado como {tipo_lista}")
            else:
                print("Tipo de lista no válido. Se utilizará ARRAY_LIST por defecto.")
                control = new_controller("ARRAY_LIST")
            print(f"Tipo de lista actual: {tipo_lista}")
            load_data_s_r(control, sample_option)
            print("Seleccione el tipo de algoritmo de ordenamiento (Selection, Insertion o Shell):")
            ordenamiento = input().lower()
            a = sortData(control, ordenamiento )
            delta_time = f"{a}"
            
            print("Para", sample_option, "elementos, delta tiempo:", str(delta_time))
            #------------------------PRINT DATOS ORDENADOS---------------------
            print(f"Tamaño de muestra seleccionado: {lt.size(control['model']['results'])}")
            print('Match result count: ' + str(lt.size(control['model']['results'])))
            print('Goal scorers count: ' + str(lt.size(control['model']['goalscore'])))
            print('shootout-penalty definition count: ' + str(lt.size(control['model']['shootouts'])))
            #--------------------MATCH RESULTS ----------------------
            print("--------------------MATCH RESULTS --------------------")
            sixResults =controller.sixdata(control['model']['results'])
            printSimpleTable(sixResults, ['date','home_team','away_team','home_score','away_score','country','city','tournament'])
           # -----------GOAL SCORES-----------------------------

        elif int(inputs) == 10:
            # TODO modificar opcion 10 del menu en el lab 5 (parte 2)
            # configurar si usa algoritmos recursivos
            rec = input("Usar algoritmos recursivos? (S/N): ")
            if rec in bool_lt_opt:
                rec = True
            else:
                rec = False



        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)

if __name__ == "__main__":

    threading.stack_size(67108864*2) # 128MB stack
    sys.setrecursionlimit(default_limit*1000000)
    thread = threading.Thread(target=menu_cycle)
    thread.start()
